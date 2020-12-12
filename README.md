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

## Development Steps: Create a Page in the Web Application
1. Create the HTML file with the page contents in the *templates* folder
2. Create a function that returns `render_templates()` where the parameter is the path to the HTML file as a string excluding the *templates* folder
3. Decorate the above function with `@app.route()` where the parameter is a string that's the URL path for the page

* To pass content from the back end to the page, add the value as the value for a keyword argument in `render_templates()` and include the variable name between two curly braces in the HTML document.

## Development Steps: Capture User Submitted Data
1. Create a `<form>` element
2. Set the `action` attribute of the `<form>` element to the URL path of the page the user will land on when the form is submitted (not including the first slash)
3. Create a page in the web application corresponding to the URL path declared above
4. Within the form, create `<input>` elements, each with a unique `name` attribute

* To capture the user input, include in the `render_template()` function for the post-submission page an assignment statement with `request.args[]` with an argument of the `name` attribute for the input element as a string.