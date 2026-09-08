
# Day 61 - Advanced Forms with Flask-WTForms

A Flask web application that uses Flask-WTF and WTForms to create and validate forms.

## Flask-WTForms
![day61](https://user-images.githubusercontent.com/98851253/161357129-4b692c13-a2b2-43ad-a63d-021ee7a301d2.gif)


## What This Project Does

The application:

1. Creates forms using Flask-WTF.
2. Adds validation to form fields.
3. Receives form data using WTForms.
4. Uses Jinja2 template inheritance.
5. Uses Flask-Bootstrap for styling forms.

## Technologies Used

* Python
* Flask
* Flask-WTF
* WTForms
* Jinja2
* Flask-Bootstrap
* HTML
* Bootstrap

## Project Structure

```text
Day-61/
│
├── main.py
├── templates/
├── README.md
├── poetry.lock
├── pyproject.toml
└── requirements.txt
```

## Installation

Install the required libraries:

```bash
pip install flask flask-wtf wtforms
```

Or:

```bash
pip install -r requirements.txt
```

## Flask-WTForms

Flask-WTF integrates WTForms with Flask and makes it easier to create and process forms.

Forms can be created using Python classes instead of writing every form field manually in HTML.

## Form Validation

WTForms allows validation rules to be added to form fields.

For example, a field can be required or can require a specific type of input.

This helps prevent invalid data from being submitted.

## Receiving Form Data

When the user submits the form, Flask-WTF processes the submitted information.

The application can then check whether the form is valid:

```python
if form.validate_on_submit():
    # Process form data
```

## Jinja Template Inheritance

The project practices template inheritance using:

```html
{% extends "base.html" %}
```

This allows templates to reuse a common layout.

## Flask-Bootstrap

Flask-Bootstrap can be used with Jinja templates to apply Bootstrap styling to forms and other webpage elements.

## Concepts Practiced

* Flask
* Flask-WTF
* WTForms
* Form creation
* Form validation
* Receiving form data
* Jinja2
* Template inheritance
* `{% extends %}`
* Bootstrap
* Flask-Bootstrap
* Python classes
* Form fields
* Validation

## Running the Project

Run:

```bash
python main.py
```

Then open:

```text
http://127.0.0.1:5000/
```

## Learning Outcome

Day 61 introduces a more structured way of creating and validating forms in Flask using Flask-WTF and WTForms.

The project also strengthens understanding of Jinja template inheritance and Bootstrap integration.

## Disclaimer

This project was created for educational purposes as part of Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp.
