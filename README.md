# [Headlines](https://headlines-vb.herokuapp.com/)
# Headlines Web App
<table>
<tr>
<td>
  A webapp showcasing the implementation of the main components for a Flask application.
</td>
</tr>
</table>


## Hosted 

- [Heroku](https://www.heroku.com/about) - Heroku is a container-based cloud Platform as a Service (PaaS).

- Check the [headlines-production](https://headlines-vb.herokuapp.com/) instance;

- !!! No split of this project in dev, staging, production since the limit for free web apps, hosted on Heroku (for free), is very small [hey, give me some money and I'll apply the full dev-cycle ;) ]


### Landing Page

![Home Page](headlines-screenshots/headlines-home.png)

### Select Publisher Option

![Select Publisher Dropdown Menu](headlines-screenshots/headlines-publisher-menu.png)

### [Development](https://github.com/vBarbaros/headlines/blob/dev/CONTRIBUTING.md)
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 

### Bug / Feature Request

If you find a bug kindly open an issue [here](https://github.com/vBarbaros/headlines/issues/new) by including the steps to reproduce it.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/vBarbaros/headlines/issues/new).


## Built with 

- [Flask](http://flask.pocoo.org/docs/1.0/) - Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It's BSD licensed!.

## Credits

- The Book [Flask: Building Python Web ServicesGareth Dwyer, Shalabh Aggarwal, Jack Stouffer](https://www.packtpub.com/web-development/flask-building-python-web-services) While using the tutorials described in this book, I made the following improvement:
	1) adapted the overall architecture of the current Flask webapp to a more reusable one;
	2) handled some potential errors, publisher-dependent (not all of them provide summaries in the feeds, etc...);
	2) refactored the app's components and prepared the necesary files to make it deployable to Heroku in a matter of seconds;

## To-do
- Add Unit Tests;
- Add CI using Travis CI;
- Improve upon app's architecture, using templates and styling;
- (...to be added, there is always stuff that can be added);


## [License](https://github.com/vBarbaros/headlines/blob/dev/LICENSE)

MIT © [Victor Barbaros](https://github.com/vBarbaros)
