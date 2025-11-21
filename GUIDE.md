## Creating a New Reflex App

### Basic Initialization

To create a new Reflex app:
```bash
uv run reflex init
# or use justfile
just init
```

**Important:** `reflex init` creates a subdirectory with your app name and generates the main configuration file `rxconfig.py` in the current directory. The structure will look like:

```
current_directory/
    rxconfig.py          # Main Reflex configuration file
     myapp/               # App directory (subdirectory with the app name)
         __init__.py
        myapp.py        # Your main app code
    assets/             # Static assets (created automatically)
```

**Note:** Some templates require authentication. Use `just login` first if you get a template access error.

### App Naming Rules

From the Reflex documentation:
- The app directory name must start with a letter
- Can contain letters, numbers, and underscores only
- No spaces or special characters

## Running Your App

Run the development server with **hot reload**:
```bash
just run
```

This starts both frontend and backend servers. The app will be available at `http://localhost:3000` by default.

## Built-in Features

**Light/Dark Mode:** Reflex apps come with light/dark mode support out of the box. No additional configuration required.

## Project Configuration Files

- `rxconfig.py` - Reflex app configuration (created after `reflex init`)
