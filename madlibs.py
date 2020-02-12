"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

STUDENTS = [
    'Liz', 'Elizabeth', 'Jenna C', 'Jenna S', 'Hana', 'Hani', 'Sweety', 'Archana'
    'Margi', 'Sandra', 'Bri', 'Lulu', 'Fabiola', 'Treanna', 'Whitney', 'Fiona'
    'Mike', 'Quynh', 'Judy', 'Jay Lynn', 'Jael', 'Lavania'
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Plays a game."""

    player = request.args.get("person")
    response = request.args.get("game")

    if response == "no":

        return render_template("goodbye.html", person=player)

    elif response == "yes":

        return render_template("game.html", player=player, student=STUDENTS)
        # return render_template("game.html", person=player)



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
