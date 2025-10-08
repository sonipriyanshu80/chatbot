def waterjug(jug1,jug2,target,maxjug1,maxjug2,visited):
    if jug1==target or jug2==target:
        print("target reached", jug1, jug2)
        return True
    if (jug1,jug2) in visited:
        return False
    visited.add((jug1,jug2))
    print("current state",(jug1,jug2))
    if waterjug(maxjug1,jug2,target,maxjug1,maxjug2,visited):
        return True
    if waterjug(jug1,maxjug2,target,maxjug1,maxjug2,visited):
        return True
    if waterjug(0,jug2,target,maxjug1,maxjug2,visited):
        return True
    if waterjug(jug1,0,target,maxjug1,maxjug2,visited):
        return True
    pour1= min(jug1,maxjug2-jug2)
    
    if waterjug(jug1-pour1,jug2+pour1,target,maxjug1,maxjug2,visited):
        return True
    #pour2= min(maxjug1-jug1,jug2)
    if waterjug(jug1+pour1,jug2-pour1,target,maxjug1,maxjug2,visited):
        return True
    return False
maxjug1=4
maxjug2=3
target=2
print("steps to reach the target")
waterjug(0,0,target,maxjug1,maxjug2,set())
    
