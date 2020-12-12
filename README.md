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

* To capture the user input, include in the `render_template()` function for the post-submission page an assignment statement with `request.args[]` with an argument of the `name` attribute for the input element as a string.

## Development Steps: Create a Redirect to a Function in app.py
1. Use `redirect(url_for())` where the innermost argument is the name of the function as a string