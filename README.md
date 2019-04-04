# automation-examples
Example Python scripts for automating workflows (primarily with MS Office products on Windows)

The scripts were intended to be run in interactive mode using Visual Studio Code with the Python plugin. They can easily be converted to Jupyter notebooks by the same plugin. The machine_learning.py script is the only script that actually needs to be run interatively to see the graphics - the other scripts all produce some visible artifact such as creating a file or launching an applicaiton.

There's examples of the following tasks:
* create_certificates.py - Creates word documents automatically.
* machine_learning.py - Demonstrates reading an Excel spreadsheet as a pandas dataframe and fitting a simple linear regression model to the data.
* scrape_website.py - Scrapes images from a website and saves them to a local directory it creates
* format_images.py - Some image manipulation to read the previously scraped images, resize them, and make them grey scale before saving to a new directory.
* create_powerpoint.py - Creates a powerpoint presentation and inserts the images created by the previous script onto new slides
* automate_windows.py - Launches and controls Windows application through the GUI
