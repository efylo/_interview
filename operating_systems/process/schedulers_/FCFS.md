# First Come First Serve (FCFS)

## Abstract

FCFS is a natural algorithm that you can see in everyday lives. For example, if you go to the Burgerking and wait for a whopper, you have to wait until previous whopper is delivered. Though, in restaurants there exist some possible exceptions, like ordering a menu that takes longer time or nobody wants will probably take longer time than ordering a whopper. 

Likewise, FCFS is ineffective in some perspective. Assume, I order a truffle mushroom whopper(menu of Burgerking Korea) which takes 15 minutes and then my friend orders a whopper that takes 3 minutes to serve. Serving a whopper to my friend firstly is far more efficient since my friend has to wait until a truffle mushroom whopper is served even though a whopper takes a lot shorter. 

This effect is called convoy effect. Waiting for a long job is quite a burden for some short jobs. Also, you cannot preempt previous job since FCFS is naturally non-preemptive. 

---

## Implementation

Advantages are inside the implementation, or progamming. Defining a simple queue is the end of programming FCFS scheduler. 

---

## Reference

- [Convoy Effect in Operating Systems](https://www.geeksforgeeks.org/convoy-effect-operating-systems/)

