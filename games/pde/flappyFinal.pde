//Flappy Bird

class Button {
  int x, y, w, h, r, g, b;
  int hoverTint = 255;
  boolean isClicked = false;
  String buttonText = "Button";
  String buttonTextHover = "Hover";
  String currentText = buttonText;
  //float w = textWidth(currentText);
  
  void update(){
    fill(r,g,b);
    rect(x,y,w,h,5);
    textSize(40);
    fill(360-r,360-g,360-b);
    text(currentText, x+5,y+40);
  }
}

PImage background, currentBird, bird;
//, bullet, enemy;
int frameBg, frameBgMax, bgLoopAmt = 1, bgX;
int frameBird, frameBirdMax;
int birdX, birdY, birdVx, birdVy;
//boolean isShooting, bull;
//int bulletX, bulletY;
String folderBg, folderBird, textRetry;
int gameState, frame, highscore, score, scoreStagger;
color bgColor;
//int enemyX, enemyY, enemyCount, enemyTimer, enemyCount2;
Button buttonFail = new Button();
Button showScore = new Button();

void setup(){
  //Setup variables
  score = 0;
  highscore = 0;
  gameState = 0;
  //isShooting = false;
  //bull = true;
  size(800,600);
  
  //setup button
  
  buttonFail.x = 90;
  buttonFail.y = 200;
  buttonFail.w = 220;
  buttonFail.h = 45;
  buttonFail.r = 90;
  buttonFail.g = 45;
  buttonFail.b = 45;
  buttonFail.buttonText = "Retry?";
  buttonFail.buttonTextHover = "Click";
  buttonFail.hoverTint = 125;
  
  //setup score button
  showScore.x = width/2;
  showScore.y = 0;
  showScore.w = 200;
  showScore.h = 45;
  showScore.r = 90;
  showScore.g = 45;
  showScore.b = 90;
  showScore.buttonText = "Score: "+score;
  showScore.buttonTextHover = "Highscore: "+highscore;
  
  folderBg = "lematworks";
  folderBird = "trianimsmall";
  textRetry = "Retry?";
  
  //Load Images
  background = loadImage("./img/"+folderBg+"/tmp-0.gif");
  //bullet = loadImage("./img/fireball.png");
  
  //Position
  birdX = width/4;
  birdY = height/2;
  frameBgMax = 44;
  
  //Records amount needed to loop
  int bgRem = width-background.width;
  while(bgRem > 0){
    bgLoopAmt++;
    bgRem -= background.width;
    print("console: background looped "+bgLoopAmt+" times");
  }
  
  //Enemy Setup - Thoe Code
  
}

void frame_advance(){
  bgX--;
  frameBg += 1;
  
  if(bgX < -background.width){
    bgX = 0;
  }
  
  if(frameBg == frameBgMax){
    frameBg = 0;
  }
}
  
void update_background(){
  image(background, 0, 0);
  image(background, bgX, 0);
  image(background, bgX+background.width, 0);
  
  if(bgLoopAmt > 1){
    image(background, bgX+background.width*2, 0);
  }
  if(bgLoopAmt > 2){
    image(background, bgX+background.width*3, 0);
  }
  if(bgLoopAmt > 3){
    image(background, bgX+background.width*4, 0);
  }
  
  background = loadImage("./img/"+folderBg+"/tmp-"+frameBg+".gif");
}

void update_bird(){
  bird = loadImage("./img/"+folderBird+"/tmp-"+frameBird+".gif");
  if(mousePressed){
    tint(255,0,0);
    int multfact = 3;
    image(bird,birdX-bird.width/multfact,birdY-bird.width/multfact);
    image(bird,birdX+bird.width/multfact,birdY-bird.width/multfact);
    image(bird,birdX-bird.width/multfact,birdY+bird.width/multfact);
    image(bird,birdX+bird.width/multfact,birdY+bird.width/multfact);
    tint(0,255,0);
  } else {
    tint(255);
  }
  image(bird,birdX,birdY);
  tint(255);
  birdY += birdVy;
  birdVy++;
}

void accelerate(){
  if(mousePressed){
    birdVy = -15;
  }
}

void check_bird(){
  if(birdY+bird.height>height+bird.height){
    gameState = 1;
  }
  if(birdY + birdVy < 0){
    birdY = 0;
    birdVy = 0;
  }
}

void drawfailbg(){
  tint(255, 100, 204);
  update_background();
  rect(0,background.height,width,height-background.height);
  tint(0);
}

void draw(){
    //show highscore
  showScore.buttonText = "Score: "+score;
  showScore.buttonTextHover = "Highscore: "+highscore;
  showScore.w = round(textWidth(showScore.currentText+1));
  if((showScore.x < mouseX)&&(mouseX < showScore.x+showScore.w)&&(showScore.y < mouseY)&&(mouseY < showScore.y+showScore.h)){
    showScore.currentText = showScore.buttonTextHover;
  } else {
    showScore.currentText = showScore.buttonText;
  }
  if(gameState == 1){
    drawfailbg();
    buttonFail.update();
    showScore.update();
    if((buttonFail.x < mouseX)&&(mouseX < buttonFail.x+buttonFail.w)&&(buttonFail.y < mouseY)&&(mouseY < buttonFail.y+buttonFail.h)){
      tint(buttonFail.hoverTint);
        if(mousePressed){
          tint(255);
          gameState = 0;
          birdY = height/4;
          scoreStagger = 0;
          score = 0;
        } else {
          buttonFail.currentText = buttonFail.buttonTextHover;
        }
      } else {
        tint(255);
        buttonFail.currentText = buttonFail.buttonText;
      }
    }else if(gameState == 0){
    scoreStagger++;
    if(scoreStagger == 20){
      scoreStagger = 0;
      score++;
    }
    if(score > highscore){
      highscore = score;
    }
    frame_advance();
    update_background();
    update_bird();
    accelerate();
    check_bird();
    showScore.update();
  }
}
