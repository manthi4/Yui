# Design considerations

* **Where should IO validation take place?** I think blocks should definetly be defined with clear strict input and output expectations. But does the actual IO validation take place when the IO objects are being created or being passed into the block?
    * In the future it may become redundent to check both the outputs and inputs
    * Do we force the user to create a new IO subclass to define new expectations? or pass expectations as a parameter when creating an IO object?
        * I think subclassing approach will result in more flexibility and control in the long run.
