/** @file game.c
 *  @authors jbr206 and obn11
 *  @date 12 October 2020
 *  @brief Rock, Paper, and Sissors game.
 */

#include "system.h"
#include "pacer.h"
#include "led.h"
#include "navswitch.h"
#include "ir_uart.h"
#include "tinygl.h"
#include "../fonts/font5x7_1.h"

#define PACER_RATE 1000
#define MESSAGE_RATE 10
#define NUM_GAMES 5
#define PAPER 'P'
#define SCISSOR 'S'
#define ROCK 'R'


/** Initialize software */
void init (void)
{
    system_init();
    navswitch_init();
    ir_uart_init();
    pacer_init (PACER_RATE);
    
    tinygl_init(PACER_RATE);
    tinygl_font_set(&font5x7_1);
    tinygl_text_speed_set(MESSAGE_RATE);
    tinygl_text_mode_set(TINYGL_TEXT_MODE_SCROLL);
}


/** Display character to UCFK4
 * @param character to display */
void display_character (char character)
{
    char buffer[2];
    buffer[0] = character;
    buffer[1] = '\0';
    tinygl_text (buffer);
}


/** Choose your letter and send to opponent
 * @param current letter */
char send_letter (char current)
{
    int done = 0;
    while (done == 0) { 
        if (navswitch_push_event_p(NAVSWITCH_NORTH)) {
            if (current == SCISSOR) {
                current = ROCK;
            } else if (current == ROCK) {
                current = PAPER ;
            } else {
                current = SCISSOR;
            }
        }
        if (navswitch_push_event_p(NAVSWITCH_SOUTH)) {
            if (current == SCISSOR) {
                current = PAPER;
            } else if (current == PAPER) {
                current = ROCK;
            } else {
                current = SCISSOR;
            }
        }
        if (navswitch_push_event_p(NAVSWITCH_PUSH)) {
            ir_uart_putc(current);
            led_set(LED1, true);
            done = 1
        }
    }
    display_character(current);
    return current;
}


/** Computes who won the game
 * @param  Both players picks*/
int check_winner (char choice[])
{
    int code;
    if (choice[0] == PAPER) {
        if (choice[1] == PAPER) {
            code = 0;
        } else if (choice[1] == SCISSOR) {
            code = 1;
        } else /*(choice[1] == ROCK)*/ {
            code = 2;
        }
    } else if (choice[0] == SCISSOR) {
        if (choice[1] == PAPER) {
            code = 2;
        } else if (choice[1] == SCISSOR) {
            code = 0;
        } else /*(choice[1] == ROCK)*/ {
            code = 1;
        }
    }
    else /*(choice[0] == ROCK)*/ {
        if (choice[1] == PAPER) {
            code = 1;
        } else if (choice[1] == SCISSOR) {
            code = 2;
        } else /*(choice[1] == ROCK)*/ {
            code = 0;
        }
    led_set(LED1, false);
    }
    return code;
}
    

/** Displays message with scroll
 * @param The period the message will be displayed for */
void display_message (int delay)
{
    int i = 0;
    while (i < delay) {
        pacer_wait();
        tinygl_update();
        navswitch_update();
        i++;
    }
    tinygl_text_mode_set(TINYGL_TEXT_DIR_NORMAL);
}


/** Welcome message */
void welcome_message (void)
{
    tinygl_text_mode_set(TINYGL_TEXT_MODE_SCROLL);
    tinygl_text("WELCOME ");
    display_message(9000);
}



/** Displays the matche results
 * @param The match result
 */
void display_match_result (int code)
{
    if (code == 0) {
        tinygl_text_mode_set(TINYGL_TEXT_MODE_SCROLL);
        tinygl_text("DRAW ");
        display_message(4500);
    }
    if (code == 1) {
        tinygl_text_mode_set(TINYGL_TEXT_MODE_SCROLL);
        tinygl_text("LOSER ");
        display_message(4500);
    }
    if (code == 2) {
        tinygl_text_mode_set(TINYGL_TEXT_MODE_SCROLL);
        tinygl_text("WINNER ");
        display_message(4500);
    }
}


/** Result message for game
 * @param player ones result
 * @param player twos result
 * @param result of game */
/*void result_message (int player1, int player2, int result)
{
    tinygl_text_mode_set(TINYGL_TEXT_MODE_SCROLL);
    if (result == 0) {
        tinygl_text("DRAW %d - %d", player1, player2);
    } else if (result == 1) {
        tinygl_text("LOSE %d - %d", player1, player2);
    } else {
        tinygl_text("WIN %d - %d", player1, plyaer2);
    }
    display_message(4500);
}*/


/** Main loop to run the game */
int run_game(void)
{
    display_character(PAPER);
    char choice[2];
    int to_send = 1;
    int to_recv = 1;
    char c = PAPER;
    int code = 3;
    while (code == 3) {
        pacer_wait();
        tinygl_update();
        navswitch_update();
        if (to_send == 1) {
            c = send_letter(c);
            choice[0] = c;
            to_send = 0;
        }
        if (ir_uart_read_ready_p() && to_recv) {
            c = ir_uart_getc ();
            if ((c == PAPER) || (c == SCISSOR) || (c == ROCK)) {
                choice[1] = c;
                to_recv = 0;
            }
        }
        if (to_recv == 0) {
            code = check_winner(choice);
            display_match_result(code);
        }
    }
    return code
}


/** Main function to initialize and looping of the game */
int main (void)
{
    init();
    led_set(LED1, false);
    welcome_message();
    display_character(PAPER);
    int i = 0;
    int your_score = 0;
    int their_score = 0;
    while (i < NUM_GAMES) {
        int code = run_game();
        if (code == 1) {
            their_score++;
        } else if (code == 2) {
            your_score++;
        }
        i++;
    }
}
