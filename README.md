# This Project gives a visual representation of the growth of Bacteria in Agar plates with few parameters to tweak and play around with.

### Pre-requisites
The Project needs some packages to be installed before running the project.
Python 3.10
- `manimce`
- `cv2 (opencv-python)`
- `matplotlib`

## The Bacteria Growth Creation
This simulates the growth of bacteria.
The Growth parameters can be tweaked from the main.py file.
to RUN:
```manimce -pql -s bacteria.py BacteriaGrowth ```
(might take a few seconds to run depending on the number of bacterias input)
This will create a video file in the media folder.

## Identifying the Colonies
Now to identify the colonies and their diameters we use a simple image processing technique through opencv.
to RUN:
```python3 imgProcess.py```
or run it through your editor

## Result
We can derive various results through our fun little animation
one of them which i derived is very intuative and simple to observe
The Result file displays the Graph between Diameter and number of colonies
to RUN:
```python3 Result.py```
or run it through your editor


### Additional Note:
All media files are stored in media folder
Bacteria on agar Plate - `media/images/main/BacteriaGrowth_ManimCE_v0.17.2.png`
Colonies on agar Plate - `media/images/main/colonies.jpg`
Result Graph - `media/images/main/Result.png`