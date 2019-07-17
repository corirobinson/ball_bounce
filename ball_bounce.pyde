ball_y=100
ball_y2=100
y_speed2=3
y_speed = 2
ball_x2=50
ball_x=50
x_speed=3
x_speed2=2
def setup():
    size(500,500)
    
    
def draw():
    global ball_y
    global y_speed
    global ball_x
    global x_speed
    global ball_y2
    global y_speed2
    global ball_x2
    global x_speed2
    background (255,255,255)
    ellipse(ball_x,ball_y,100,100)
    ellipse(ball_x2,ball_y2,100,100)
    strokeWeight(5)
    line (0,400,500,400)
    
    
 
    if ball_y > 350:
        y_speed=-y_speed 
    if ball_y > 350:         #>ball 1
        fill(52,132,255)
        
    if ball_y2 > 350:
        y_speed2=-y_speed2 
    if ball_y2 > 350:        #>ball2
        fill(52,132,255)
            
    if ball_y< 50:
        y_speed=4
    if ball_y< 50:           #>ball 1
        fill(255,46,152)
        
    if ball_y2< 50:
        y_speed2=4           #>ball2
    if ball_y2< 50:
        fill(255,46,152)

    if ball_x < 50 : 
        x_speed=-x_speed  
    if ball_x < 50 :         #>ball 1
        fill(130,250,130)
        
    if ball_x2 < 50 : 
        x_speed2=-x_speed2    #>ball2
    if ball_x2 < 50 : 
        fill(130,250,130)
         
    if ball_x>450:
        x_speed=-x_speed
    if ball_x>450:
        fill(2550,100,30)    #>ball 1
        
    if ball_x2>450:
        x_speed2=-x_speed2    #>ball2
    if ball_x2>450:
        fill(2550,100,30)
        
        
        
    ball_x=ball_x+x_speed  
    ball_y= ball_y+y_speed  
    ball_x2=ball_x2+x_speed2  
    ball_y2= ball_y2+y_speed2  
   
   
             
    
    
    
