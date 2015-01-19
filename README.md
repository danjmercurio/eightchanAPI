# eightchanAPI
A Python API for 8chan
## Example

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
## Dependencies
* requests

## Thanks
* Frederick Brennan
* Guido Van Rossum
