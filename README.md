### Part 1:  Raichu
**Algorithm used**- Minimax with alpha-beta pruning

**Initial State**- Any given board can be the start state

**Successors**-All the possible combinations of board where each piece(Raichu,Pikachu and Pichu) make all the legal moves

**Moves**-A set of legal moves for the state

**Evaluation Function**-We used a weighted linear function to make the best move on any given state.
                        If the current player is the white player,
                        Evaluation function= (white Raichu - black Raichu) + (white Pikachu-black Pikachu) + (white Pichu black                         pichu).
                        If the current playes is black,
                        Evaluation function= (black Raichu - white Raichu) + (black Pikachu-white Pikachu) + (black Pichu -white                         pichu).
                        
**Terminal test**- Due to large branching factor, the search would take a lot of time to reach the leaf node of the game tree. A                    horizon(depth) had to be set and results were backed up from this depth using the evaluation function.

**Action**- Choose the move that has the highest score(largest backed up value)
-game tree
-horizon concept

#### Approach-
This two-player,turn-taking and deterministic game could be best solved using adverserial search. We started with implementing Minimax algorithm. But since the branching factor for each state was large, it was taking a long time to reach deeper into the Game Tree preventing it from making better decisions. To reduce this enormous state space, we used alpha-beta pruning to trim the useless nodes. We timed both the codes and the simple Minimax algorithm took 18 secs to yield an output at depth 3 and Minimax with alpha-beta pruning took just 3 secs to reach the same depth. This was a significant improvement and gave us better solutions by searching deeper into the game tree.

#### Challenges-
We spent a lot of time deciding the weights for each of the pieces in the Evaluation function and then testing it with different players. We noticed that increasing the weights of Raichu made our player play better. The Pikachus and Pichus started moving forward towards the end of board to become Raichu as soon as the game started. The weight assigned to Raichu was #, weight assigned to Pikachu was #, and weight assigned to Pichu was #.
Another thing we noticed while testing our AI against AIs of classmates was that recommending a random move to AI where evaluation function gave same score worked better in the average case than just giving the first move among the moves yielding the same best scores.

### Part 2: The Game of Quintris

**Initial State:** Given empty state board

**State Space** All states possible after each new piece is generated.


#### Set of Sucessors:
For the current piece falling on the baord:
We have defined the sucessors according to all possible moves it can take to fall in different orientations on the board. For this we have used the column number which is the left upper column number defined already in the program. 
For any column number we have defined the valid moves of the piece on the board. 

For the next piece:
Here, for next piece the moves taken by the piece does not matter. The different orientations and placings that the next piece can be in on the board state (given that current piece has already fallen) matters. So we have set the row number and column number to zero as default and finding the all possible places the piece can fall and in all possible orientations.

#### Heursitic Function:

We have used weighted sum of three heuristic fucntions for this game.

Heuristic 1: Our Heuristic evaluates the state's correctness according the number of holes in the state and assigns weights to those holes according to thier location. We reffered the research paper in following link to write the heuristic function.

http://kth.diva-portal.org/smash/get/diva2:815662/FULLTEXT01.pdf 

According to above document,a hole is defined as follows:
1. An empty cell to the left of a column in which the topmost cell is at the same height or above the empty cell in question.
2. An empty cell under the topmost filled cell in the same column.
3. An empty cell to the right of a column in which the topmost cell is at the same height or above the empty cell in question.

Heuristic 2: The total height of all the columns on the board state. Here, we are trying to minimize the height of the board so that the baord doesnt get filled up. If the pieces reach maximum height, then the game will be over.

Heuristic 3: The third heuristic is the number of cleared lines after the piece is placed. 

The weights are assigned as follows:
Total heuristic value: Heuristic1 + Heuristic2 - 25 * Heursitic3
#### Approach:

**Simple:** Here we are going for depth 2 uptil the successors for next piece are calculated. So, at first we are finding the successors for the current state of the board using the current piece that is falling and the position from which it is falling from. Then, for all the successors we are calculating the successors (for all possible configurations of the board and piece) using the next piece. We are calculating the heuristic value for each of the sucessors of next piece. The minimum of heuristic value will be backed up. The moves taken to get that minimum heuristic successor are then returned to make those moves.
We also tried implementing the Expectimin algorithm (as we are trying to minimize heuristic value) but the algorithm was taking around 10 to 12 minutes for placing one piece.

We got the highest score of 450 till now.

**Animated:** The approach here is almost same as that of the simple version. Here we are going for depth 2 uptil the successors for next piece are calculated. So, at first we are finding the successors for the current state of the board using the current piece that is falling and the position from which it is falling from. Then, for all the successors we are calculating the successors (for all possible configurations of the board and piece) using the next piece. We are calculating the heuristic value for each of the sucessors of next piece. The minimum of heuristic value will be backed up. The moves taken to get that minimum heuristic successor are then made in order to place that current piece. 
This process is repeated as new piece gets generated.

#### Challenges:
We were struggling to find where actually the chnace concept fit in here as the next piece was already given. But then we understood that it first 2 depths will be deterministic but after that depth there will a chance of getting the pieces from the given 6 pieces. 
We tried to implement Expectimin (as our heuristic is to be minimized) algorithm by using the distribution of probability which is defined at start of every game. The ExpectiMin Algorithm is working but its taking a lot of time to place a piece. 

### Part 3: Truth be told

#### Aim: 
The aim of this question is to use naive bayes classifier to classify hotel reviews as truthful and deceptive.

#### Background:

Naive Bayes is a classification technique based on Bayes theorem. 
The bayes theorem is given by:

P(A|B,C)=(P(B,C|A) * P(A))/ P(B,C)

Here, A,B,C are events.
P(A|B,C) is the probability of A given B and C. This is also called posterior probability.
P(B,C|A) is the probability of B and C given A. This is also called likelihood probability.
P(A) is the probability of A. This is also called prior probability of A.
P(B,C) is the probability of B and C. This is also called prior probability of B and C.

In naive bayes, it assumes that the 2 events B and C are independent of each other. Therefore, the likelihood probability P(B,C|A) is equal to P(B|A) * P(C|A). 

For the given problem, event A can be that the given document is truthful or deceptive and event B and C (and more) can be the words in the document.


#### Approach:

For a given document, we first seperated all the words (tokenization) to calculate it's counts. We created a count dictionary that contained the word as the key. The value parameter of this dictionary was another dictionary which had 2 keys: truthful and deceptive. The value of this was the count of that word in the respective label. For example, if the word 'unfortunately', is seen in truthful data 5 times and deceptive data 10 times, then the dictionary representation would be {'unfortuantely':{'deceptive':10,'truthful':5}}
We also calculated the total unique words for the truthful and deceptive labels. 

This count dictionary was then used to calculate probabilities of words given their labels (truthful and deceptive). That is the likelihood probabilities. These probabilities were also stored in the similar way. These likelihood probabilities are calculated on the train data. After calculating the likelihood probabilities, we calculate the posterior probability. The posterior probabilities are calculated for both labels and they are compared to give final result. 

#### Challenges:

First, we started by only doing tokenization of the document. This gave us an accuracy of 53%. To improve the accuracy, we tried data processing techniques like removing punctuations, removing numbers, and using lower case for all words. This increased our accuracy to 57%. To handle unseen data from test set, we set small probabilities to words that are not present in training set. Moreover, we also set small probabilities to words which are present only in one label. For example, if the word 'gross' only comes in truthful data and not in deceptive data then it's probability for deceptive is set to 0.1. By doing this we got the accuracy as 77.5%. We played around with stop words and the accuracy was increased to 79.25%. 

To increase the probability more, we tried using log probabilities. This resulted in an accuarcy of 84.25%







