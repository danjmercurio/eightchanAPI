# eightchanAPI
A Python API for 8chan
## Examples

### Get some info on a board
```python
>>> import eightchanAPI
>>> eightchanAPI.getBoard('v')
<8chan /v/ board instance object at 0x0000000003C3A548>
>>> eightchanAPI.getBoard('v').isSFW()
False
>>> eightchanAPI.getBoard('v').title
u'Video Games'
>>> eightchanAPI.getBoard('v').subtitle
u'Vidya Games'
>>> eightchanAPI.getNumBoards()
4114
```
### Get the first post on each board
```python
>>> import eightchanAPI
>>> boards = eightchanAPI.getBoards()
>>> for board in boards:
        print board.firstThread().firstPost().comment
```
### Did the OP get doubles?
```python
>>> import eightchanAPI
>>> eightchanAPI.getBoard('k').getThread(454584).firstPost().checkDubs()
True
```
### Get all of the images from a thread
```python
>>> import eightchanAPI
>>> thread = eightchanAPI.getBoard('a').getThread(398594).getAllFileURLs()
```
### ...or just the sixth one
```python
>>> import eightchanAPI
>>> files = eightchanAPI.getBoard('a').getThread(398594).getPosts()[5].getFileURLs()
```

## Dependencies
* requests
* json

## Shoutouts
* Frederick Brennan
* Guido Van Rossum
