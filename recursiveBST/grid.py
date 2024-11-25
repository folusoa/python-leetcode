def equalPairs(grid):
        
        row = ""
        col = ""
        count = 0

        arrS = set()


        for i in range(len(grid)): 
            for j in range(len(grid[i])): 

                col += str(grid[j][i])
                row += str(grid[i][j])
                
            if row == col or row in arrS or col in arrS: 
                count += 1

            arrS.add(col)
            row = col = ""
  
        return count
         

def main(): 
     
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    #grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(equalPairs(grid))

if __name__ == "__main__": 
     main()