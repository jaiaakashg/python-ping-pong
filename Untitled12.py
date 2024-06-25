#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import display, HTML

display(HTML('''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Pong Game</title>
<style>
    body {
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #000;
    }
    canvas {
        border: 1px solid #fff;
        background-color: #000;
    }
    .scoreboard {
        position: absolute;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        color: #fff;
        font-size: 24px;
    }
</style>
</head>
<body>
<div class="scoreboard" id="scoreboard">Player 1: 0 | Player 2: 0</div>
<canvas id="pongCanvas" width="600" height="400"></canvas>
<script>
    const canvas = document.getElementById('pongCanvas');
    const context = canvas.getContext('2d');
    const scoreboard = document.getElementById('scoreboard');

    const paddleWidth = 10;
    const paddleHeight = 100;
    const ballSize = 10;
    let player1Y = canvas.height / 2 - paddleHeight / 2;
    let player2Y = canvas.height / 2 - paddleHeight / 2;
    let ballX = canvas.width / 2;
    let ballY = canvas.height / 2;
    let ballSpeedX = 4;
    let ballSpeedY = 2;
    let player1Score = 0;
    let player2Score = 0;

    function drawPaddle(x, y) {
        context.fillStyle = '#fff';
        context.fillRect(x, y, paddleWidth, paddleHeight);
    }

    function drawBall(x, y) {
        context.fillStyle = '#fff';
        context.fillRect(x, y, ballSize, ballSize);
    }

    function moveBall() {
        ballX += ballSpeedX;
        ballY += ballSpeedY;

        if (ballY <= 0 || ballY >= canvas.height - ballSize) {
            ballSpeedY = -ballSpeedY;
        }

        if (ballX <= paddleWidth) {
            if (ballY > player1Y && ballY < player1Y + paddleHeight) {
                ballSpeedX = -ballSpeedX;
            } else {
                player2Score++;
                updateScoreboard();
                resetBall();
            }
        }

        if (ballX >= canvas.width - paddleWidth - ballSize) {
            if (ballY > player2Y && ballY < player2Y + paddleHeight) {
                ballSpeedX = -ballSpeedX;
            } else {
                player1Score++;
                updateScoreboard();
                resetBall();
            }
        }
    }

    function resetBall() {
        ballX = canvas.width / 2;
        ballY = canvas.height / 2;
        ballSpeedX = -ballSpeedX;
    }

    function updateScoreboard() {
        scoreboard.textContent = `Player 1: ${player1Score} | Player 2: ${player2Score}`;
    }

    function draw() {
        context.clearRect(0, 0, canvas.width, canvas.height);
        drawPaddle(0, player1Y);
        drawPaddle(canvas.width - paddleWidth, player2Y);
        drawBall(ballX, ballY);
        moveBall();

        requestAnimationFrame(draw);
    }

    canvas.addEventListener('mousemove', function(event) {
        const canvasPosition = canvas.getBoundingClientRect();
        player1Y = event.clientY - canvasPosition.top - paddleHeight / 2;
        if (player1Y < 0) player1Y = 0;
        if (player1Y > canvas.height - paddleHeight) player1Y = canvas.height - paddleHeight;
    });

    draw();
</script>
</body>
</html>
'''))

