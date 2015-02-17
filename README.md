# infinitechan-api
## Description
A Python API for 8chan

## Features
* List all boards
* View board details
* List all threads in specific board
* List all posts in specific thread
* Read post comment
* Download post image

## System Requirements
* Python 2.7.x

## Dependencies
* requests
* json
* pep8

## Build Instructions
There are no build instructions, basically make sure you import the api header like this.

```python
from infinitechanapi import *
```

That's it! You are now ready to interact with 8chan. Read the usage section to see how to use this API.

## Usage (Examples)
### List All Boards
```python
from infinitechanapi import *
api = InifinitechanAPI()
boards = api.get_boards();
print(boards)
```

### View Board Details
```python
from infinitechanapi import *
api = InifinitechanAPI()
tech = api.get_board('/tech/')
print(tech)
```

### Get Comment
```python
from infinitechanapi import *
api = InifinitechanAPI()
tech = api.get_board('/tech/')
first_thread = tech.first_thread()
comment = first_thread.first_post().comment
print(comment)
```

## License
This API is licensed under the GNU Lesser General Public License. See [LICENSE.md](LICENSE.md) for more information.

## Shoutouts
* Frederick Brennan
* Guido Van Rossum
