Get email notifications when your long-running python script dies unexpectedly. No dependencies, no API keys, minimal config: just two lines at the top of your script.

```python
import crashcanary
crashcanary.init('example@gmail.com')

print('Doing dangerous things...')
print(4/0)
```
Produces:

![Sample Email](https://raw.githubusercontent.com/revan/crashcanary/master/crash.png)
