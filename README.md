# Action Grammar

The naive case pipe line (development stage):<br>

1. segment out the blocks out of the space. (using the masking method is this case)
2. label the objects in the segmented image
3. So we got the objects in the image, now do the objects contacting each other part. If two 
objects are in contact with each other, we need to detect that. How to do that? 
Assuming the objects in the space won't move by themselves. Only the "Robot" can move them.<br>
When the "Robot" is not touching anything but is moving, define it as a "free object"<br>
When the "Object" is not moving, define it as a "dead object" <br>
Object States:<br>
Robot (red) -> state1 not moving (dead), state2 moving but not touching (free), state3 moving and touching (operate)<br>
Objects (not-robot) -> state1 not moving (dead), state2 moving (being operated)
4. Define a general tree data structure (possibly multiway tree). Define nodes of 2 types: external and internal. External nodes are only at the leaf level, representing the objects, such as the blue object being operated by the robot. Internal nodes represent the robot kinetics, such as moving to left, right x units, rotating xx degrees etc. Note: this kind of data structure might change in the future.