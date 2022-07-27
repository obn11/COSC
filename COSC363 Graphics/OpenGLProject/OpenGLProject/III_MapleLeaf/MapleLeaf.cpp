//  ========================================================================
//  COSC363: Computer Graphics (2021);  University of Canterbury.
//
//  FILE NAME: MapleLeaf.cpp
//  See Lab03_ObjectModelling.pdf  for details
//  ========================================================================

#include <iostream>
#include <cmath>
#include <GL/freeglut.h>
#include "loadBMP.h"
using namespace std;

GLuint txId;
float angle = 0;    //Rotation angle
const int N = 21;   //Number of vertices
float vx[] = { 2, 2, 13, 11, 14, 9, 9, 4, 6, 3, 0, -3, -6, -4, -9, -9, -14, -11, -13, -2, -2 };
float vy[] = { 0, 4, 8, 9, 13, 13, 15, 11, 22, 20, 25, 20, 22, 11, 15, 13, 13, 9, 8, 4, 0 };
float XMIN = -14;
float XMAX = 14;
float YMIN = 0;
float YMAX = 25;

float s(float x)
{  
    return (x - -14) / (14 - -14);
}

float t(float y)
{
    return (y - 0) / (25 - 0);
}


void loadTexture()
{
    glGenTextures(1, &txId); 				// Create a Texture object
    glBindTexture(GL_TEXTURE_2D, txId);		//Use this texture
    loadBMP("WoodTexture.bmp");
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);	//Set texture parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);
}
//-- Ground Plane --------------------------------------------------------
void drawFloor()
{
    glDisable(GL_LIGHTING);
    glColor3f(0.7, 0.7,  0.7);          //Floor colour

    for(int i = -200; i <= 200; i +=5)
    {
        glBegin(GL_LINES);          //A set of grid lines on the xz-plane
            glVertex3f(-200, -0.1, i);
            glVertex3f(200, -0.1, i);
            glVertex3f(i, -0.1, -200);
            glVertex3f(i, -0.1, 200);
        glEnd();
    }
}

//-----------------------------------------------------------------------
void initialise(void)
{
    float grey[4] = {0.2, 0.2, 0.2, 1.0};
    float white[4]  = {1.0, 1.0, 1.0, 1.0};
    float black[4] = { 0, 0, 0, 1 };

    glEnable(GL_DEPTH_TEST);
    glEnable(GL_NORMALIZE);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glLightfv(GL_LIGHT0, GL_AMBIENT, grey);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, white);
    glLightfv(GL_LIGHT0, GL_SPECULAR, white);
    glEnable(GL_SMOOTH);

    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, black);
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, white);
    glEnable(GL_COLOR_MATERIAL);
    loadTexture();
    glBindTexture(GL_TEXTURE_2D, txId);

    glClearColor (1.0, 1.0, 1.0, 0.0);

    glMatrixMode (GL_PROJECTION);
    glLoadIdentity ();
    gluPerspective(30.0, 1.0, 20.0, 500.0);
}

//-------------------------------------------------------------------
// Computes the normal vector of a triangle/quad
void normal(float x1, float y1, float z1,
            float x2, float y2, float z2,
              float x3, float y3, float z3 )
{
      float nx, ny, nz;
      nx = y1*(z2-z3)+ y2*(z3-z1)+ y3*(z1-z2);
      ny = z1*(x2-x3)+ z2*(x3-x1)+ z3*(x1-x2);
      nz = x1*(y2-y3)+ x2*(y3-y1)+ x3*(y1-y2);

      glNormal3f(nx, ny, nz);
}

//-----------------The base polygon  ------------------------
void drawBase()
{
    glBegin(GL_POLYGON);
    for (int i = 0; i < N; i++)
        glVertex3f(vx[i], vy[i], 0);
    glEnd();
}

void drawTriangulated()
{
    glBegin(GL_TRIANGLE_FAN);
        glTexCoord2f(s(0), t(6));
        glVertex3f(0, 6, 0);
        for (int i = 0; i < N; i++) {
            glTexCoord2f(s(vx[i]), t(vy[i]));
            glVertex3f(vx[i], vy[i], 0);
        }
        glVertex3f(vx[0], vy[0], 0);
    glEnd();
}

void drawModel()
{
    

    glPushMatrix();
        glNormal3f(0, 0, -1);
        glTranslatef(0, 0, -1);
        drawTriangulated();
    glPopMatrix();

    glPushMatrix();
        glNormal3f(0, 0, 1);    
        glTranslatef(0, 0, 1);
        drawTriangulated();
    glPopMatrix();

    glBegin(GL_QUAD_STRIP);
    for (int i = 0; i < N; i++)
    {
        glVertex3f(vx[i], vy[i], -1); //Vertices on the first polygon
        if (i > 0) normal(vx[i - 1], vy[i - 1], -1,
            vx[i], vy[i], -1,
            vx[i], vy[i], 1);
        glVertex3f(vx[i], vy[i], 1); //Vertices on the second polygon
    }
    glEnd();

}

void drawShadowModel(float lgt_pos[])
{
    
    float shadowMat[16] = {lgt_pos[1],0,0,0, -lgt_pos[0],0,-lgt_pos[2],-1, 0,0,lgt_pos[1],0, 0,0,0,lgt_pos[1] };
    glDisable(GL_LIGHTING);
    glDisable(GL_TEXTURE_2D);

    glPushMatrix(); //Draw Shadow Object
        glMultMatrixf(shadowMat);
        /* Object Transformations */
        glColor4f(0.2, 0.2, 0.2, 1.0);
        drawModel(); 
        glDisable(GL_TEXTURE_2D);
    glPopMatrix();

    glEnable(GL_LIGHTING);
    glDisable(GL_TEXTURE_2D);

    glPushMatrix(); //Draw Actual Object
    /* Transformations */
        glColor3f(235.0/255, 45.0/255, 55.0/255);
        glEnable(GL_TEXTURE_2D);
        drawModel();
    glPopMatrix();
}
//-------------------------------------------------------------------
void display(void)
{
    float lgt_pos[] = {40.0f, 100.0f, 100.0f, 1.0f};
    glDisable(GL_TEXTURE_2D);
    glClear (GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
    
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0., 25, 100.0, 0., 10., 0., 0., 1., 0.);

    glRotatef(angle, 0, 1, 0);      //Rotate the entire scene

    glLightfv(GL_LIGHT0, GL_POSITION, lgt_pos);   //light position (not used as lighting is disabled)

    glColor3f (0.0, 1.0, 1.0);
    glDisable(GL_TEXTURE_2D);
    glPushMatrix(); //Draw Actual Object
    /* Transformations */
    glDisable(GL_TEXTURE_2D);
    drawShadowModel(lgt_pos);
    glPopMatrix();
    

    drawFloor();
    glEnable(GL_LIGHTING);
    glDisable(GL_TEXTURE_2D);
    glFlush();
}

//--------------------------------------------------------------------------------
void special(int key, int x, int y)
{
    if(key==GLUT_KEY_LEFT) angle --;
    else if(key==GLUT_KEY_RIGHT) angle ++;

    glutPostRedisplay();
}

//-------------------------------------------------------------------
int main(int argc, char** argv)
{
   glutInit(&argc, argv);
   glutInitDisplayMode (GLUT_SINGLE| GLUT_DEPTH);
   glutInitWindowSize (600, 600);
   glutInitWindowPosition (100, 100);
   glutCreateWindow ("Maple Leaf");
   initialise ();
   glutDisplayFunc(display);
   glutSpecialFunc(special);
   glutMainLoop();
   return 0;
}
