# Evodoc Backend

*Backend v2, new and better*

## Contribution

1. Use virtualenv for development (ie. `source venv/bin/activate`)
2. Use branches, each feature should have its own branch, when you think everything is done just create PR to master. You can freely merge things into dev branch.
3. When you are coming back to your branch, first of all do `git rebase master` to catch up with other contributors.
4. Write clean and easy-to-read code, also use documentation string on each function/method/class. :)

## How to run app as developer

1. Create and or enter into virtualenv for >=python3.6
2. Just run `pip install -e .`
3. Enter into your virtualenv or edit `venv/bin/acitvate` script
4. Export these values or write them into activation script:
    ```
    export FLASK_APP=evodoc
    export FLASK_DEBUG=1
    export FLASK_ENV="development"
    ```
5. (only if you are editing `activate`): save your script and re-enter into venv
6. Just type `flask run`
7. ???
8. Profit