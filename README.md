# Flask_Across_Docker--Public
Setting up a Flask site to serve as a web app for a database across a series of Docker containers. This is the public repository containing the web app itself.

## Moving to Flask Development Server
1. Open bash shell
2. `export FLASK_ENV=development`
3. `flask run`
4. Go to web address provided by output

## Development Steps: Setup
1. Create file *app.py* (default name--allows for starting built-in server without specifying app name)
2. Create folder *templates* to hold HTML template files
3. Create folder *static* to hold CSS, images, and other static files

## Development Steps: Create a Page in the Web Application
1. Create the HTML file with the page contents in the *templates* folder
2. Create a function that returns `render_template()` where the parameter is the path to the HTML file as a string excluding the *templates* folder
3. Decorate the above function with `@app.route()` where the parameter is a string that's the URL path for the page

* To pass content from the back end to the page, add the value as the value for a keyword argument in `render_template()` and include the variable name between two curly braces in the HTML document.

## Development Steps: Capture User Submitted Data via POST Request
1. Create a `<form>` element on the HTML page that will collect the data
2. For that element, set the `action` attribute to the URL path of the page the user will land on when the form is submitted (not including the first slash) and the `method` attribute to `'POST'`
3. In *app.py*, set up the route matching the above URL route with the additional argument `methods=['GET', 'POST']`
4. Create the function decorated by the above route with a `if request.method == 'POST':` that returns the `render_template()` for the page the user should be directed to upon submitting the form and an `else:` with a redirect
5. Create the HTML file referenced in the `render_template()` above (if not already created)
6. Within the `<form>` element, create `<input>` elements, each with a unique `name` attribute

* To capture the user input, include in the function decorated by the route for the post-submission page `request.form[]` with an argument of the `name` attribute for the input element as a string.
* To make use of the value on the webpage via jinja, the `render_template()` function must include a keyword argument where the argument name is the value used in the HTML wrapped in jinja's double curly braces and the value is what will be displayed when the HTML renders.

## Development Steps: Create a Redirect to a Function in app.py
1. Use `redirect(url_for())` where the innermost argument is the name of the function as a string

## Development Steps: Flash a Message When Landing on a Page
0. Ensure *app.py* has a `app.secret_key` value
1. In *app.py*, just before the `return` statement that renders the HTML template for the page, add `flash()` with an argument of a string that contains the message that should be displayed to the user
2. On the page's HTML file, add the jinja for loop elements `{% for message in get_flashed_messages() %}` and `{% endfor %}` (`message` in the loop start is a variable name and can be changed to any value in that declaration, but message makes sense)
3. Between the jinja loop elements, add `{{ message }}` (the name of the variable in the for loop in jinja's double curly braces) within any HTML tags that should be applied to the text of the flashed message

## Development Steps: Allow Users to Upload Files via POST Request
1. Create a `<form>` element on the HTML page that will collect the data
2. For that element, set the `action` attribute to the URL path of the page the user will land on when the form is submitted (not including the first slash), the `method` attribute to `'POST'`, and the `enctype` to `'multipart/form-data'`
3. Do steps 3-5 from "Capture User Submitted Data via POST Request"
4. Within the `<form>` element, create an `<input>` element with the attribute `type='file'` and a unique `name` attribute
5. Create other `<input>` elements within the `<form>`, each with a unique `name` attribute
6. Within the function decorated by the route to the HTML file specified in the `action` attribute, save the file to a location in the project directory with `request.files[].save()` with the value of the `name` attribute for the input element as a string in the brackets and the full file path and name of the file as a string in the parentheses. (Note: all files in the path must exist before the saving attempt for it to work)

## Development Steps: Create a Variable URL Route
1. Create a route function decorator `@app.route('/<string:variable>')`
2. Define a route function which takes `variable` as a parameter

* When a given URL route not matching one of the static routes preceeding the variable URL function is entered, the value of the path is passed into the function as a string. Generally speaking, this variable should be cross-referenced against some other data source with potential values for `variable` and corresponding other data that will be provided when the page loads via jinja; otherwise, all possible paths on the domain will be considered valid.

## Development Steps: Serve a File Saved in Static
1. `return redirect(url_for('static', filename=))` where the value of the `filename` keyword argument is the file path to the file to be served from the *static* folder (meaning not including that folder, but including all subfolders)

## Development Steps: Setting Up a 404 Page
Look up best practice for how to do this--is "if a variable route URL function was activated, but the URL route itself didn't match anything we have data for, return 404" the best practice?
1. Set up page with variable route URL
2. For the inability to find a match to the value passed into the function, `return abort(404)`
3. Create a function with a parameter `error` containing `return render_template('page_not_found.html'), 404` (the HTML file name can be anything, but page_not_found is appropriate)
4. Decorate the above function with `@app.errorhandler(404)`

## Development Steps: Internal Linking with Jinja
1. `<a href="{{ url_for() }}">link text<a>` where the parameter for `url_for` is the name of the function decorated by the URL path that the link should go to as a string

## Development Steps: Create a HTML Template
1. Create a HTML file
2. Add `{% block block_name %}` and `{% endblock %}` to the body of the template where `block_name` is the name of the block that will be inserted into the template
3. In the HTML file with the content to be inserted into the template, add `{% extends 'file.html' %}` where file is the name of the template (at the beginning of the file???)
4. In that same HTML file, wrap the content that should be rendered on the page between `{% block block_name %}` and `{% endblock %}`

* Blocks can be included in the head.

## Development Steps: Create a Function for Executing SQL Statements
1. Create a function to return a connection object
   1. `return <module used for connectiong to MySQL>.connect(host='host', user='root', password='password', database='database)`
   2. `'Host'` is the host of the MySQL server as a string, `'password'` is the password for the root user, `'database'` is the name of the database/schema being used and is optional (if left out, must be declared later)