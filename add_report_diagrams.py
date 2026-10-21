from pathlib import Path
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


ROOT = Path(r"D:\Mini_project")
REPORT = ROOT / "Certify_Project_Report.docx"
DIAGRAM_DIR = ROOT / "_report_diagrams"
DIAGRAM_DIR.mkdir(exist_ok=True)


def box(ax, x, y, w, h, text, color="#DCEAF7", fontsize=10):
    patch = FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.03",
        linewidth=1.5, edgecolor="#1F4E79", facecolor=color,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, wrap=True)


def arrow(ax, start, end, text=None):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=16,
                                 linewidth=1.3, color="#333333"))
    if text:
        ax.text((start[0] + end[0]) / 2, (start[1] + end[1]) / 2 + 0.06,
                text, ha="center", va="center", fontsize=8)


def save_architecture():
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.set_xlim(0, 11); ax.set_ylim(0, 6); ax.axis("off")
    box(ax, .4, 4.4, 2.2, .8, "User Browser\nThymeleaf + JavaScript")
    box(ax, 4.4, 4.4, 2.2, .8, "CertificateController\nGET /view, POST /save")
    box(ax, 8.4, 4.4, 2.2, .8, "CertificateService\nValidation + generation")
    arrow(ax, (2.6, 4.8), (4.4, 4.8), "HTTP")
    arrow(ax, (6.6, 4.8), (8.4, 4.8), "form model")
    box(ax, 3.0, 1.4, 2.2, .8, "CertificateContainer\nMultipartFile + fields")
    box(ax, 7.0, 1.4, 2.2, .8, "Local File System\nPNG + certificates.zip")
    arrow(ax, (5.5, 4.4), (4.1, 2.2), "binds")
    arrow(ax, (9.5, 4.4), (8.1, 2.2), "writes")
    ax.set_title("Figure 4.1: Certify System Architecture", fontsize=14, weight="bold")
    fig.tight_layout()
    path = DIAGRAM_DIR / "architecture.png"
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return path


def save_use_case():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.axis("off")
    ax.add_patch(plt.Rectangle((2.2, .7), 6.5, 5.6, fill=False,
                               linewidth=1.5, edgecolor="#1F4E79"))
    ax.text(5.45, 6.05, "CERTIFY SYSTEM", ha="center", fontsize=13, weight="bold")
    ax.text(1.0, 3.7, "User", ha="center", fontsize=11, weight="bold")
    ax.plot([1, 1], [3.1, 4.2], color="black", linewidth=1.5)
    ax.plot([.6, 1.4], [3.8, 3.8], color="black", linewidth=1.5)
    ax.plot([1, .6], [3.1, 2.4], color="black", linewidth=1.5)
    ax.plot([1, 1.4], [3.1, 2.4], color="black", linewidth=1.5)
    cases = [(3.2, 4.8, "Upload template"), (5.5, 4.8, "Upload CSV"),
             (3.2, 3.4, "Select name position"), (5.5, 3.4, "Set font size"),
             (3.2, 2.0, "Generate certificates"), (5.5, 2.0, "Download ZIP")]
    for x, y, label in cases:
        ax.add_patch(plt.Circle((x + .95, y), .48, fill=False,
                                linewidth=1.2, edgecolor="#2E75B6"))
        ax.text(x + .95, y, label, ha="center", va="center", fontsize=8)
        ax.plot([1.35, x + .47], [3.0, y], linestyle="--", color="#555555")
    ax.set_title("Figure 4.2: Use Case Diagram", fontsize=14, weight="bold")
    fig.tight_layout()
    path = DIAGRAM_DIR / "use_case.png"
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return path


def save_sequence():
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.set_xlim(0, 11); ax.set_ylim(0, 8); ax.axis("off")
    actors = [(1.0, "User"), (3.3, "Browser"), (5.6, "Controller"),
              (7.9, "Service"), (10.0, "File System")]
    for x, label in actors:
        ax.text(x, 7.5, label, ha="center", weight="bold")
        ax.plot([x, x], [1, 7.2], linestyle="--", color="#777777")
    messages = [
        (6.7, 1.0, 3.3, "Open /view"),
        (5.9, 3.3, 5.6, "POST /save"),
        (5.1, 5.6, 7.9, "generateCertificates"),
        (4.3, 7.9, 10.0, "write PNG files"),
        (3.5, 7.9, 10.0, "create ZIP"),
        (2.7, 7.9, 5.6, "return File"),
        (1.9, 5.6, 3.3, "download response"),
    ]
    for y, x1, x2, label in messages:
        arrow(ax, (x1, y), (x2, y), label)
    ax.set_title("Figure 4.3: Certificate Generation Sequence Diagram",
                 fontsize=14, weight="bold")
    fig.tight_layout()
    path = DIAGRAM_DIR / "sequence.png"
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return path


def save_activity():
    fig, ax = plt.subplots(figsize=(9, 8))
    ax.set_xlim(0, 9); ax.set_ylim(0, 11); ax.axis("off")
    steps = [(4, 9.8, "Start"), (3.2, 8.5, "Upload template and CSV"),
             (4.0, 7.1, "Select coordinates and font size"),
             (3.7, 5.7, "Validate inputs"), (4.0, 4.3, "Read participant names"),
             (3.5, 2.9, "Generate PNG certificates"),
             (4.0, 1.5, "Create ZIP and download"), (4, .3, "End")]
    for i, (x, y, label) in enumerate(steps):
        if label in ("Start", "End"):
            ax.add_patch(plt.Circle((x, y), .38, color="#D9EAD3", ec="#38761D"))
        else:
            ax.add_patch(FancyBboxPatch((x - 1.25, y - .35), 2.5, .7,
                                        boxstyle="round,pad=.03", fc="#DCEAF7",
                                        ec="#1F4E79"))
        ax.text(x, y, label, ha="center", va="center", fontsize=9)
        if i < len(steps) - 1:
            arrow(ax, (x, y - .4), (steps[i + 1][0], steps[i + 1][1] + .4))
    ax.set_title("Figure 4.4: Certificate Generation Activity Diagram",
                 fontsize=14, weight="bold")
    fig.tight_layout()
    path = DIAGRAM_DIR / "activity.png"
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return path


def set_update_fields(doc):
    settings = doc.settings.element
    update = settings.find(qn("w:updateFields"))
    if update is None:
        update = OxmlElement("w:updateFields")
        settings.append(update)
    update.set(qn("w:val"), "true")


def replace_toc_instruction(doc):
    for paragraph in doc.paragraphs:
        if paragraph.text.strip() == "The following contents are organized according to the supplied project-report format. In Microsoft Word, right-click the Table of Contents field and choose “Update Field” after opening the document to populate page numbers.":
            paragraph.text = "The Table of Contents below is configured to display headings and page numbers. If page numbers are not refreshed automatically, right-click the table and select “Update Field” → “Update entire table”."
        for field in paragraph._p.findall(".//" + qn("w:fldSimple")):
            instruction = field.get(qn("w:instr"), "")
            if instruction.startswith("TOC"):
                field.set(qn("w:instr"), 'TOC \\o "1-3" \\h \\z \\u')


def add_diagram_section(doc, images):
    doc.add_page_break()
    h = doc.add_heading("Appendix C: Formal Diagrams", level=1)
    doc.add_paragraph("This appendix provides formal visual representations of the system architecture and principal user workflow.")
    captions = [
        ("System Architecture", images[0], "Figure C.1: Certify System Architecture"),
        ("Use Case Diagram", images[1], "Figure C.2: Use Case Diagram"),
        ("Sequence Diagram", images[2], "Figure C.3: Certificate Generation Sequence Diagram"),
        ("Activity Diagram", images[3], "Figure C.4: Certificate Generation Activity Diagram"),
    ]
    for title, image, caption in captions:
        doc.add_heading(title, level=2)
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(image), width=Inches(6.2))
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(caption)
        r.italic = True
        r.font.size = Pt(9)


def main():
    images = [save_architecture(), save_use_case(), save_sequence(), save_activity()]
    doc = Document(REPORT)
    set_update_fields(doc)
    replace_toc_instruction(doc)
    add_diagram_section(doc, images)
    doc.save(REPORT)
    print(REPORT)


if __name__ == "__main__":
    main()
