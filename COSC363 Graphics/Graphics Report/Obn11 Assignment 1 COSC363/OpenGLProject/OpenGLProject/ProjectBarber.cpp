#include <iostream>
#include <cmath>
#include <GL/freeglut.h>
#include "loadBMP.h"
#define GL_CLAMP_TO_EDGE 0x812F
using namespace std;


const int N = 9;
const float PI = 3.14159265;
const float detail = 10.0;
const float theta = (detail * PI) / 180;
float vxB_init[N] = { 0,  2.8, 3, 3.7, 4,  4.5,    4.5,  3,  0 };
float vyB_init[N] = { 15, 15, 14, 14,  14, 11.5, 11, 10, 10 };
float vzB_init[N] = { 0 };
float thota = 0;
float thoti = 0;
float cycleTracker = 0;
float lgt_pos[] = { 50.0f, 100.0f, 100.0f, 1.0f };
float angle = -0.4, eye_x = 20-(40*sin(angle)), eye_z = ((30 * cos(angle)) + 60), look_x = eye_x + 100 * sin(angle), look_z = eye_z - 100 * cos(angle);  
float sbd = 200;
float rev = 1;
float rev2 = 1;
float shadowMat[16] = { lgt_pos[1],0,0,0, -lgt_pos[0],0,-lgt_pos[2],-1, 0,0,lgt_pos[1],0, 0,0,0,lgt_pos[1] };

GLuint txId[8];


//------Function to load a texture in bmp format  ------------------------
void loadTexture()
{
	glGenTextures(8, txId); 				
	glBindTexture(GL_TEXTURE_2D, txId[0]);		
	loadBMP("BarberTexture.bmp");
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE);


	glBindTexture(GL_TEXTURE_2D, txId[1]);		
	loadBMP("up.bmp");
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);	
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);


	glBindTexture(GL_TEXTURE_2D, txId[2]);		
	loadBMP("down.bmp");
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);	
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);


	glBindTexture(GL_TEXTURE_2D, txId[3]);	
	loadBMP("left.bmp");
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);	
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);


	glBindTexture(GL_TEXTURE_2D, txId[4]);		
	loadBMP("right.bmp");
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);	
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);


	glBindTexture(GL_TEXTURE_2D, txId[5]);		
	loadBMP("front.bmp");
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);	
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);


	glBindTexture(GL_TEXTURE_2D, txId[6]);	
	loadBMP("back.bmp");
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);	
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);


	glBindTexture(GL_TEXTURE_2D, txId[7]);	
	loadBMP("bottom.bmp");
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);
}

//------------------------------------------------------------------------
void myTimer(int value)
{
	thota += (10*rev);
	cycleTracker++;
	if (cycleTracker > 90) {
		glutSolidSphere(3, 5, 5); 
		thoti += (20*rev2);
		thota -= (10*rev);
		if (cycleTracker == 98) rev*= -1;
		if (cycleTracker > 107) cycleTracker = 0, rev2*=-1;
	}
	glutPostRedisplay();
	glutTimerFunc(50, myTimer, 0);
}

//-------------------------------------------------------------------
void initialise(void)
{
	float grey[4] = { 0.2, 0.2, 0.2, 1.0 };
	float white[4] = { 1.0, 1.0, 1.0, 1.0 };
	float black[4] = { 0, 0, 0, 1 };
	loadTexture();

	glEnable(GL_DEPTH_TEST);
	glEnable(GL_NORMALIZE);
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
	glLightfv(GL_LIGHT0, GL_AMBIENT, grey);
	glLightfv(GL_LIGHT0, GL_DIFFUSE, white);
	glLightfv(GL_LIGHT0, GL_SPECULAR, white);
	glEnable(GL_SMOOTH);

	glClearColor(1.0, 1.0, 1.0, 1.0);

	glEnable(GL_COLOR_MATERIAL);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(40.0, 1.0, 20.0, 500.0);
}

//-------------------------------------------------------------------
void normal(float x1, float y1, float z1,
	float x2, float y2, float z2,
	float x3, float y3, float z3, bool neg)
{
	float nx, ny, nz;
	nx = y1 * (z2 - z3) + y2 * (z3 - z1) + y3 * (z1 - z2);
	ny = z1 * (x2 - x3) + z2 * (x3 - x1) + z3 * (x1 - x2);
	nz = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2);

	if (neg) glNormal3f(-nx, -ny, -nz);
	else glNormal3f(nx, ny, nz);
}

//-------------------------------------------------------------------
void drawBase(bool isShadow)
{
	if (!isShadow) glEnable(GL_TEXTURE_2D);
	glBindTexture(GL_TEXTURE_2D, txId[7]);
	float vx[N], vy[N], vz[N];
	float wx[N], wy[N], wz[N];

	for (int i = 0; i < N; i++)		
	{
		vx[i] = vxB_init[i];
		vy[i] = vyB_init[i];
		vz[i] = vzB_init[i];
	}

	for (int j = 0; j < (360 / detail); j++) 
	{
		for (int i = 0; i < N; i++) 
		{
			wx[i] = vx[i] * cos(theta) + vz[i] * sin(theta);
			wy[i] = vy[i];
			wz[i] = -vx[i] * sin(theta) + vz[i] * cos(theta);
		}
		glBegin(GL_TRIANGLE_STRIP); 
		for (int i = 0; i < N; i++) {
			if (i > 0) normal(vx[i - 1], vy[i - 1], vz[i - 1],
				wx[i - 1], wy[i - 1], wz[i - 1],
				vx[i], vy[i], vz[i],true);
			glTexCoord2f((float)j / 36, (float)i/(N-1));
			glVertex3f(vx[i], vy[i], vz[i]);
			if (i > 0) normal(wx[i - 1], wy[i - 1], wz[i - 1],
				wx[i], wy[i], wz[i],
				vx[i], vy[i], vz[i],true);
			glTexCoord2f((float)j / 36, (float)i / (N - 1));
			glVertex3f(wx[i], wy[i], wz[i]);
		}
		glEnd();
		
		for (int i = 0; i < N; i++)
		{
			vx[i] = wx[i];
			vy[i] = wy[i];
			vz[i] = wz[i];
		}
	}
	glDisable(GL_TEXTURE_2D);
}

//-------------------------------------------------------------------
void drawCylinder(bool isShadow)
{
	double vx2[2], vy2[2], vz2[2];
	double wx2[2], wy2[2], wz2[2];

	if (!isShadow) glEnable(GL_TEXTURE_2D);
	glBindTexture(GL_TEXTURE_2D, txId[0]);

	for (int i = 0; i < 2; i++)		
	{
		vx2[i] = 2.546479089;
		vy2[i] = (i*16);
		vz2[i] = 0;
	}

	float t = (0.17578125 * PI) / 180;
	for (int j = 0; j < 2048; j++) 
	{
		for (int i = 0; i < 2; i++) 
		{
			wx2[i] = vx2[i] * cos(t) + vz2[i] * sin(t);
			wy2[i] = vy2[i];
			wz2[i] = -vx2[i] * sin(t) + vz2[i] * cos(t);
		}
		
		glBegin(GL_TRIANGLE_STRIP); 
		for (int i = 0; i < 2; i++) {
			if (i > 0) normal(vx2[i - 1], vy2[i - 1], vz2[i - 1],
				wx2[i - 1], wy2[i - 1], wz2[i - 1],
				vx2[i], vy2[i], vz2[i],false);
			glTexCoord2f((float)j / 2048, (float)i);
			glVertex3f(vx2[i], vy2[i], vz2[i]);

			if (i > 0) normal(wx2[i - 1], wy2[i - 1], wz2[i - 1],
				wx2[i], wy2[i], wz2[i],
				vx2[i], vy2[i], vz2[i],false);
			glTexCoord2f((float)(j + 1) / 2048, (float)i);
			glVertex3f(wx2[i], wy2[i], wz2[i]);
		}
		glEnd();
		
		
		for (int i = 0; i < 2; i++)
		{
			vx2[i] = wx2[i];
			vy2[i] = wy2[i];
			vz2[i] = wz2[i];
		}

	}
	glFlush();
	glDisable(GL_TEXTURE_2D);
}

//-------------------------------------------------------------------
void drawSkybox(void)
{
	glEnable(GL_TEXTURE_2D);
	glBindTexture(GL_TEXTURE_2D, txId[5]);


	glBegin(GL_QUADS);
	glNormal3f(0, 0, 1);
	glTexCoord2f(1, 0); glVertex3f(-sbd, -1.1, -sbd); //front
	glTexCoord2f(0, 0); glVertex3f(sbd, -1.1, -sbd);
	glTexCoord2f(0, 1); glVertex3f(sbd, sbd, -sbd);
	glTexCoord2f(1, 1); glVertex3f(-sbd, sbd, -sbd);
	glEnd();

	glBindTexture(GL_TEXTURE_2D, txId[6]);
	glBegin(GL_QUADS);
	
	glTexCoord2f(0, 0); glVertex3f(-sbd, -1.1, sbd); //back
	glTexCoord2f(1, 0); glVertex3f(sbd, -1.1, sbd);
	glTexCoord2f(1, 1); glVertex3f(sbd, sbd, sbd);
	glTexCoord2f(0, 1); glVertex3f(-sbd, sbd, sbd);
	glEnd();


	glBindTexture(GL_TEXTURE_2D, txId[3]);
	glBegin(GL_QUADS);
	
	glTexCoord2f(0, 0); glVertex3f(-sbd, -1.1, -sbd); //left
	glTexCoord2f(1, 0); glVertex3f(-sbd, -1.1, sbd);
	glTexCoord2f(1, 1); glVertex3f(-sbd, sbd, sbd);
	glTexCoord2f(0, 1); glVertex3f(-sbd, sbd, -sbd);
	glEnd();

	
	glBindTexture(GL_TEXTURE_2D, txId[4]);
	glBegin(GL_QUADS);

	glTexCoord2f(1, 0); glVertex3f(sbd, -1.1, -sbd); //right
	glTexCoord2f(0, 0); glVertex3f(sbd, -1.1, sbd);
	glTexCoord2f(0, 1); glVertex3f(sbd, sbd, sbd);
	glTexCoord2f(1, 1); glVertex3f(sbd, sbd, -sbd);
	glEnd();


	glBindTexture(GL_TEXTURE_2D, txId[1]);
	glBegin(GL_QUADS);
	glTexCoord2f(1, 1); glVertex3f(-sbd, sbd, -sbd); //up
	glTexCoord2f(0, 1); glVertex3f(-sbd, sbd, sbd);
	glTexCoord2f(0, 0); glVertex3f(sbd, sbd, sbd);
	glTexCoord2f(1, 0); glVertex3f(sbd, sbd, -sbd); 
	glEnd();

	
	glBindTexture(GL_TEXTURE_2D, txId[2]);
	glBegin(GL_QUADS);
	glTexCoord2f(1, 0); glVertex3f(-sbd, -1.1, -sbd); // down
	glTexCoord2f(0, 0); glVertex3f(-sbd, -1.1, sbd);
	glTexCoord2f(0, 1); glVertex3f(sbd, -1.1, sbd);
	glTexCoord2f(1, 1); glVertex3f(sbd, -1.1, -sbd);
	glEnd();


	glDisable(GL_TEXTURE_2D);
}

//-------------------------------------------------------------------
void drawPole(bool isShadow)
{
	glPushMatrix();
	if (!isShadow) glColor3f(1.0, 1.0, 1.0);
	glTranslatef(0, 12, 0);
	glutSolidSphere(3, 20, 20);
	glPopMatrix();

	glPushMatrix();
	if (!isShadow) glColor3f(0.6, 0.6, 0.6);
	glTranslatef(0, 2, 0);
	drawBase(isShadow);
	glPopMatrix();

	glPushMatrix();
	if (!isShadow) glColor3f(1.0, 1.0, 1.0);
	glTranslatef(0, 16, 0);
	glRotatef(thota, 0, 1, 0);
	drawCylinder(isShadow);
	glPopMatrix();

	glPushMatrix();
	if (!isShadow) glColor3f(0.6, 0.6, 0.6);
	glTranslatef(0, 26, 0);
	glTranslatef(0, 10, 0);
	glRotatef(180, 1, 0, 0);
	glTranslatef(0, -10, 0);
	drawBase(isShadow);
	glPopMatrix();

	glPushMatrix();
	if (!isShadow) glColor3f(1.0, 1.0, 1.0);
	glTranslatef(0, 39, 0);
	glutSolidSphere(3.5, 20, 20);
	glPopMatrix();

}

//-------------------------------------------------------------------
void display(void)
{

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	gluLookAt(eye_x, 70, eye_z, look_x, 10, look_z, 0, 1, 0);
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINES);
	glRotatef(angle, 0, 1, 0);		
	glLightfv(GL_LIGHT0, GL_POSITION, lgt_pos); 
	glColor3f(1.0, 1.0, 0.0);    
	glEnable(GL_LIGHTING);

	glDisable(GL_LIGHTING);
	glDisable(GL_TEXTURE_2D);

	glPushMatrix(); //Draw Shadow Object
		glTranslatef(-17, 0, -34);
		glRotatef(thoti, 0, 1, 0);
		glTranslatef(17, 0, 34);
		glMultMatrixf(shadowMat);
		glColor4f(0.2, 0.2, 0.2, 1.0);
		glColor3f(0.1, 0.1, 0.1);
		drawPole(true);
	glPopMatrix();

	glEnable(GL_LIGHTING);

	glPushMatrix();
		glTranslatef(0, 24, 0);
		glRotatef(thoti, 0, 0, 1);
		glTranslatef(0, -24, 0);
		drawPole(false);
	glPopMatrix();


	glPushMatrix();
		drawSkybox();
	glPopMatrix();


	glutSwapBuffers();
}

//--------------------------------------------------------------------------------
void special(int key, int x, int y)
{
	if (key == GLUT_KEY_LEFT) angle-=0.05;       
	else if (key == GLUT_KEY_RIGHT) angle+=0.05;
	else if (key == GLUT_KEY_DOWN)
	{  //Move backward
		eye_x -= 0.5 *sin(angle);
		eye_z += 0.5 * cos(angle);
	}
	else if (key == GLUT_KEY_UP)
	{ //Move forward
		eye_x += 0.5 * sin(angle);
		eye_z -= 0.5 * cos(angle);
	}

	look_x = eye_x + 100 * sin(angle);
	look_z = eye_z - 100 * cos(angle);
	glutPostRedisplay();
}

//-------------------------------------------------------------------
int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(100, 100);
	glutCreateWindow("Barber");
	initialise();
	glutDisplayFunc(display);
	glutTimerFunc(50, myTimer, 0);
	glutSpecialFunc(special);
	glutMainLoop();
	return 0;
}