# mtg-ontology

An ontology describing Magic: The Gathering. It provides a data model to represent cards, their costs and rules.

The ontology is available in multiple representations in the [project/](project/) folder. It is also distributed as a python package providing dataclasses for the different concepts, and helpers to convert them to RDF graphs.

It can be installed wjth

```python
pip install mtg-ontology
```

## Website

* [https://cmdoret.net/mtg_ontology](https://cmdoret.net/mtg_ontology)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
    * [mtg_ontology](src/mtg_ontology)
        * [schema](src/mtg_ontology/schema) -- LinkML schema (edit this)
* [datamodel](src/mtg_ontology/datamodel) -- Generated python datamodel
* [tests](tests/) - python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

- `make all`: make everything
- `make deploy`: deploys site

</details>

## Credits

this project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)
