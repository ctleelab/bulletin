from biblib import algo, bib  # https://github.com/aclements/biblib
import sys
import warnings
from string import Template
from textwrap import dedent
import datetime
from pathlib import Path
from typing import List, Tuple

## CONFIGURATION
base_path = Path("papers")
bib_file = Path("_scripts/ctleelab.bib")


def clean():
    for file in base_path.glob("_posts/*.md"):
        file.unlink()


pub_mkdwn_template = Template(
    dedent(
        """\
    ---
    layout: paper
    title: $TITLE
    authors: $AUTHORS

    journal: $JOURNAL
    doi: $DOI
    shortcite: $SHORTCITE
    citation: $CITATION

    image: $IMAGE
    pdf: $PDF
    supplement: $SUPPLEMENT

    biorxiv: $BIORXIV
    arxiv: $ARXIV
    chemrxiv: $CHEMRXIV

    github: $GITHUB
    zenodo: $ZENODO
    
    date: $DATE

    status: $STATUS
    inprep: $INPREP
    ---

    # Abstract

    $ABSTRACT
    """
    )
)


def format_author_line(authors: str, annotations: str) -> str:
    """Parse authors and annotations to produce a complete author text string.

    Args:
        authors (str): authors
        annotations (str): annotations dictionary string

    Returns:
        str: _description_
    """
    names = algo.parse_names(authors)

    formatted_names = []
    author_string = ""
    for name in names:
        # Convert first names to initials
        first = ". ".join([part[0] for part in name.first.split(" ")]) + "."
        formatted_names.append(f"{first} {name.last}")

    # Convert annotations string to dict
    annotations_dict = dict()
    an_auth = annotations.split(";")
    for auth in an_auth:
        tmp = auth.split("=")
        k = int(tmp[0])
        v = [x.strip() for x in tmp[1].split(",")]
        annotations_dict[k] = v

    # Generate formatted string
    for i in range(1, len(formatted_names) + 1):
        tmp = formatted_names[i - 1]
        if i in annotations_dict:
            if "coauth" in annotations_dict[i]:
                tmp += "<sup>*</sup>"
            if "corresponding" in annotations_dict[i]:
                tmp += "<sup>$</sup>"
            # if "highlight" in annotations_dict[i]:
            #     tmp = "<b>" + tmp + "</b>"
        if i == 1:
            author_string += tmp
        elif i == len(formatted_names):
            author_string += f", and {tmp}"
        else:
            author_string += f", {tmp}"
    return author_string


def process_bib():
    with open(bib_file, "r") as fp:
        db = bib.Parser().parse(fp, log_fp=sys.stderr).get_entries()

    for entry in db.values():

        if entry.typ == "article":
            print(f"Parsing {entry.typ}: {entry.key}")

            # Prepopulate arxiv, biorxiv, chemrxiv, pmcid
            preprints = {
                "biorxiv": "",
                "chemrxiv": "",
                "pmcid": "",
                "arxiv": "",
            }

            # Parse for related preprint entries
            if "related" in entry and entry["related"] != "":
                for related in entry["related"].split(","):
                    related_item = db[related.strip().lower()]
                    preprints[related_item["eprinttype"].strip()] = related_item[
                        "eprint"
                    ]

            date = datetime.date.fromisoformat(entry["date"])
            authors = algo.parse_names(entry["author"])

            d = {
                "KEY": entry.key,
                "TITLE": f"'{algo.tex_to_unicode(entry['title'])}'",
                "AUTHORS": f"'{format_author_line(entry['author'], entry['author+an'])}'",
                "BIORXIV": preprints["biorxiv"],
                "ARXIV": preprints["arxiv"],
                "CHEMRXIV": preprints["chemrxiv"],
                "DATE": entry["date"],
                "ABSTRACT": entry["abstract"],
                "GITHUB": "",
                "ZENODO": "",
            }

            def parse_published():
                # nonlocal entry, date, authors, d
                citation = f"{entry['volume']}"
                if "number" in entry:
                    citation += f".{entry['number']} ({date.strftime('%B %Y')})"
                else:
                    citation += f" ({date.strftime('%B %Y')})"

                if "pages" in entry:
                    citation += f", pp. {entry['pages']}"

                d.update(
                    {
                        "INPREP": False,
                        "DOI": entry["doi"],
                        "CITATION": f"'{citation}'",
                        "STATUS": "",
                    }
                )

            if "shortjournaltitle" in entry:
                d.update(
                    {
                        "JOURNAL": f"'{entry['shortjournaltitle']}'",
                        "SHORTCITE": f"{authors[0].last}{' et al.,' if len(authors) > 0 else ''} {date.strftime('%Y')} {entry['shortjournaltitle']}",
                    }
                )
            else:  # Use full journal title
                d.update(
                    {
                        "JOURNAL": f"'{entry['journaltitle']}'",
                        "SHORTCITE": f"{authors[0].last}{' et al.,' if len(authors) > 0 else ''} {date.strftime('%Y')} {entry['journaltitle']}",
                    }
                )

            if "github" in entry:
                d.update({"GITHUB": entry["github"]})
            if "zenodo" in entry:
                d.update({"ZENODO": entry["zenodo"]})
            if "image" in entry:
                d.update({"IMAGE": entry["image"]})
            if "website" in entry:
                d.update({"WEBSITE": entry["website"]})
            if "pdf" in entry:
                d.update({"PDF": entry["pdf"]})
            if "supplement" in entry:
                d.update({"SUPPLEMENT": entry["supplement"]})

            if "entrysubtype" in entry:
                ## PARSE FOR PREPRINTS
                if entry["entrysubtype"] == "unpublished":
                    d.update(
                        {
                            "INPREP": True,
                            "JOURNAL": f"'{entry['pubstate']}'",
                            "DOI": "",
                            "CITATION": "",
                            "STATUS": f"'{entry['pubstate']}'",
                            "SHORTCITE": f"{authors[0].last}{' et al.,' if len(authors) > 0 else ''} {date.strftime('%Y')} {entry['pubstate']}",
                        }
                    )
                elif entry["entrysubtype"] == "":
                    parse_published()
                else:
                    warnings.warn(
                        f"Unknown entry subtype {entry['entrysubtype']} for item {entry.key}"
                    )
            else:
                # No subtype assume published
                parse_published()

            result = pub_mkdwn_template.substitute(d)

            with open(f"{base_path}/_posts/{entry['date']}-{entry.key}.md", "w") as fd:
                fd.write(result)

        elif entry.typ == "incollection":
            print(f"Parsing incollection: {entry.typ}: {entry.key}")
            # Prepopulate arxiv, biorxiv, chemrxiv, pmcid
            preprints = {
                "biorxiv": "",
                "chemrxiv": "",
                "pmcid": "",
                "arxiv": "",
            }

            # Parse for related preprint entries
            if "related" in entry and entry["related"] != "":
                for related in entry["related"].split(","):
                    related_item = db[related.strip().lower()]
                    preprints[related_item["eprinttype"].strip()] = related_item[
                        "eprint"
                    ]

            date = datetime.date.fromisoformat(entry["date"])
            authors = algo.parse_names(entry["author"])

            d = {
                "KEY": entry.key,
                "TITLE": f"'{algo.tex_to_unicode(entry['title'])}'",
                "AUTHORS": f"'{format_author_line(entry['author'], entry['author+an'])}'",
                "BIORXIV": preprints["biorxiv"],
                "ARXIV": preprints["arxiv"],
                "CHEMRXIV": preprints["chemrxiv"],
                "DATE": entry["date"],
                "ABSTRACT": entry["abstract"],
                "GITHUB": "",
                "ZENODO": "",
            }

            citation = f"Vol. {entry['volume']}. ({date.strftime('%B %Y')})"
            if "pages" in entry:
                citation += f", pp. {entry['pages']}"

            d.update(
                {
                    "INPREP": False,
                    "DOI": entry["doi"],
                    "CITATION": f"'{citation}'",
                    "STATUS": "",
                }
            )

            d.update(
                {
                    "JOURNAL": f"'{entry['series']}'",
                    "SHORTCITE": f"{authors[0].last}{' et al.,' if len(authors) > 0 else ''} {date.strftime('%Y')} {entry['series']}",
                }
            )

            if "github" in entry:
                d.update({"GITHUB": entry["github"]})
            if "zenodo" in entry:
                d.update({"ZENODO": entry["zenodo"]})
            if "image" in entry:
                d.update({"IMAGE": entry["image"]})
            if "website" in entry:
                d.update({"WEBSITE": entry["website"]})
            if "pdf" in entry:
                d.update({"PDF": entry["pdf"]})
            if "supplement" in entry:
                d.update({"SUPPLEMENT": entry["supplement"]})

            result = pub_mkdwn_template.substitute(d)

            with open(f"{base_path}/_posts/{entry['date']}-{entry.key}.md", "w") as fd:
                fd.write(result)

        elif entry.typ == "phdthesis":
            print("skip phd thesis")
        elif entry.typ == "online":
            pass
        else:
            print("Skipping...", entry.typ, ":", entry.key)


if __name__ == "__main__":
    clean()
    process_bib()
