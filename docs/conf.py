import pathlib
import wget
import zipfile

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
templates_path = ["_templates"]
project = "EE System"
extensions = [
    "sphinx_panels",
    "sphinxcontrib.plantuml",
    "sphinx.ext.githubpages",
]
exclude_patterns = [
    "_build/**",
]
panels_add_bootstrap_css = False

docs_path = pathlib.Path(__file__).parent.absolute()
plantuml_path = docs_path / "plantuml.jar"
if not plantuml_path.exists():
    print("Downloading PlantUml")
    wget.download(
        "https://sourceforge.net/projects/plantuml/files/plantuml.1.2020.19.jar/download",
        str(plantuml_path),
    )
jlatex_path = docs_path / "jlatexmath.zip"
if not jlatex_path.exists():
    wget.download("http://beta.plantuml.net/plantuml-jlatexmath.zip", str(jlatex_path))
    with zipfile.ZipFile(jlatex_path, "r") as zip:
        zip.extractall(path=docs_path)
plantuml = f"java -jar {plantuml_path} -I{pathlib.Path(__file__).parent.absolute()}/style.plantuml"
plantuml_output_format = "svg_img"
