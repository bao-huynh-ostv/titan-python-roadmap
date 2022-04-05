# ***Virtual environment***

## -  *Create virtual environment*

> **`python -m venv [PATH_TO_NEW_VIRTUAL_ENV]`**
>
> **`source  <venv>/bin/activate`** *'activate' the created virtual env (`<venv>` is the path of directory containing the virtual env)*
>
> **`deactivate`** *deactivate the virtual env*

## -  *Install **poetry** in osx / linux / bashonwindows*
>
> **`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -`**
>
> **`export PATH="$HOME/.poetry/bin:$PATH"`**
>
>> ### -  *Install **poetry** with `pip`*
>>
>> **`pip install poetry`**
>

## -  *Poetry usage*

> **`poetry new [NEW_PROJECT_NAME]`** *create new project*
>
> **`poetry init`** *initialise a pre-existing project*
>
> **`poetry add [PACKAGE]`** *automatically find a suitable version constraint and **install** the package and subdependencie*
>
> **`poetry install`** *install defined dependencies*
