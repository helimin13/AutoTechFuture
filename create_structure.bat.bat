@echo off
echo Creating AutoTech Future Project Structure...

REM Create directories
mkdir static\css
mkdir static\js
mkdir static\images
mkdir static\uploads
mkdir templates
mkdir data

REM Create Python files
type nul > app.py
type nul > models.py
type nul > config.py
type nul > ai_content.py
type nul > setup.py
type nul > requirements.txt
type nul > run.bat
type nul > windows_setup.bat

REM Create HTML templates
type nul > templates\base.html
type nul > templates\index.html
type nul > templates\blog.html
type nul > templates\blog_detail.html
type nul > templates\future_tech.html
type nul > templates\create_post.html
type nul > templates\login.html
type nul > templates\register.html
type nul > templates\3d_visualization.html
type nul > templates\404.html
type nul > templates\500.html

REM Create static files
type nul > static\css\style.css
type nul > static\js\main.js

echo Structure created successfully!
pause