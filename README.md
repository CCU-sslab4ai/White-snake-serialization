# White-snake-serialization

白蛇傳劇本的序列化

## Python usage

```python
import json
with open('result.json', encoding='utf8') as f:
  data = json.loads(f.read())
print(data[0]) // Chapter 1
```
