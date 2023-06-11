# action_grammar

The pipe line:<br>

1. segment out the blocks out of the space. (using the masking method is this case)
2. label the objects in the segmented image
3. So we got the objects in the image, now do the objects contacting each other part. If two 
objects are in contact with each other, we need to detect that. How to do that? 
Assuming the objects in the space won't move by themselves. Only the "Robot" can move them.
When the "Robot" is not touching anything but is moving, define it as a "free object"
When the "Object" is not moving, define it as a "dead object"

