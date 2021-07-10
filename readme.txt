- a small python program using breadth-first search algorithm to identify shortest path to exit.
+ find button takes current maze layout and applies the algorithm on it
+ reset button, its in the name; back to blank maze
= left clicking on maze blocks turns them black meaning "obstacle", reclicking turns it back to white
= pressing "E" on any maze block turns it into an "exit" block
= pressing "S" on any maze block turns it into a "start" block
* any of the above actions overrides the state of the mazeblock
* blocking the start from the end bugs out. runs forever