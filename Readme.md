# Samples 201
Provides a set of functions that call the [Samples 101 functions](https://github.com/nerdguru/samples101) in various order.  Namely, reverseStarWars, weatherReverse, and weatherStarWars.

## Usage
Using the sample is simple and demonstrated in `usage.py`:
```
import samples201
import samples101
import sys

print(samples201.reverseStarWars('hello'))
print(samples201.weatherReverse('New Orleans', sys.argv[1]))
print(samples201.weatherStarWars('New Orleans', sys.argv[1]))
```
And to execute:
```
python usage.py XXXXXXX
```
where `XXXXXXX` represents your [OpenWeather API key](https://openweathermap.org/api).  That execution should yield:
```
  ______    __       __       _______  __    __  
 /  __  \  |  |     |  |     |   ____||  |  |  |
|  |  |  | |  |     |  |     |  |__   |  |__|  |
|  |  |  | |  |     |  |     |   __|  |   __   |
|  `--'  | |  `----.|  `----.|  |____ |  |  |  |
 \______/  |_______||_______||_______||__|  |__|


elzzird ytisnetni thgil
 __       __    _______  __    __  .___________.
|  |     |  |  /  _____||  |  |  | |           |
|  |     |  | |  |  __  |  |__|  | `---|  |----`
|  |     |  | |  | |_ | |   __   |     |  |     
|  `----.|  | |  |__| | |  |  |  |     |  |     
|_______||__|  \______| |__|  |__|     |__|     

 __  .__   __. .___________. _______ .__   __.      _______. __  .___________.
|  | |  \ |  | |           ||   ____||  \ |  |     /       ||  | |           |
|  | |   \|  | `---|  |----`|  |__   |   \|  |    |   (----`|  | `---|  |----`
|  | |  . `  |     |  |     |   __|  |  . `  |     \   \    |  |     |  |     
|  | |  |\   |     |  |     |  |____ |  |\   | .----)   |   |  |     |  |     
|__| |__| \__|     |__|     |_______||__| \__| |_______/    |__|     |__|     

____    ____
\   \  /   /
 \   \/   /  
  \_    _/   
    |  |     
    |__|     

 _______  .______       __   ________   ________   __       _______
|       \ |   _  \     |  | |       /  |       /  |  |     |   ____|
|  .--.  ||  |_)  |    |  | `---/  /   `---/  /   |  |     |  |__   
|  |  |  ||      /     |  |    /  /       /  /    |  |     |   __|  
|  '--'  ||  |\  \----.|  |   /  /----.  /  /----.|  `----.|  |____
|_______/ | _| `._____||__|  /________| /________||_______||_______|

```
