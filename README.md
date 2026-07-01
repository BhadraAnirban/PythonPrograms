




…or create a new repository on the command line
echo "# PythonPrograms" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/BhadraAnirban/PythonPrograms.git
git push -u origin main



…or push an existing repository from the command line
git remote add origin https://github.com/BhadraAnirban/PythonPrograms.git
git branch -M main
git push -u origin main


Execute below line after pull the project first time from github in your system-
pip install -r requirements.txt