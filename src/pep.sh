echo "Auto formatting Python files..."

# Run autopep8 on python files in this directory and in sub directories
python3 -m autopep8 --in-place -aaaaaaaa --max-line-length 79 *.py
python3 -m autopep8 --in-place -aaaaaaaa --max-line-length 79 */*.py

# Find if any python files are not pep8 compliant
find . -name '*.py' -exec pep8 {} +

# Let the user know it's okay to commit and push
if [ $? -eq 0 ]; then
    echo "All's good, you can commit and push!"
fi
