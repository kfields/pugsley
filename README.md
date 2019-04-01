# Pugsley

### Installation

1. Navigate to a directory somewhere where you keep your software projects:

        cd projects

2. Clone the repository:

        git clone https://github.com/kfields/pugsley.git
        
3. Navigate to the new directory which contains the repository.

        cd pugsley

4. Create a Python 3 virtual environment called `env`:

        python3 -m venv env
        
5. Activate the environment:

        source env/bin/activate
        
6. Install required packages:

        pip install -r requirements.txt


### Running the website

1. Activate the virtual environment, if not already active:

        cd pugsley
        source env/bin/activate
        
2. Launch the Flask application:

        $ ./dev

### Modifying the blog database
        python manage.py makemigrations blog
        python manage.py migrate blog

### Inspecting the blog database
        python manage.py shell
        >>> from blog.models import Post
        >>> Post.objects.all()