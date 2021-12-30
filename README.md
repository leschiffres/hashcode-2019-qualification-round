# Google Hashcode 2019 - Qualification Round

## Brief Description

Given a list of photos with tags that describe them, the goal is to find a permutation (i.e. put the photos side by side), so that the sequence is as **interesting** as possible.

The interesting factor of two tag lists $S_1, S_2$  is defined as the minimum of: 
$$min(|S_1-S_2|, |S_2-S_1|, |S_1 \cap S_2|)$$

Thus, two consecutive photos must be neither identical nor completely irrelevant.

## Implemented Algorithms