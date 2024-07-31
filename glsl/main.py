import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import math

def load_shader(shader_file):
    with open(shader_file, 'r') as file:
        shader_source = file.read()
    return str(shader_source)

def create_shader_program(vertex_shader_source, fragment_shader_source):
    vertex_shader = compileShader(vertex_shader_source, GL_VERTEX_SHADER)
    fragment_shader = compileShader(fragment_shader_source, GL_FRAGMENT_SHADER)
    program = compileProgram(vertex_shader, fragment_shader)
    return program

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    vertex_shader_source = load_shader('vertex_shader.glsl')
    fragment_shader_source = load_shader('fragment_shader.glsl')
    shader_program = create_shader_program(vertex_shader_source, fragment_shader_source)

    vertices = [
        -0.5, -0.5, 0.0,
         0.5, -0.5, 0.0,
         0.0,  0.5, 0.0
    ]
    vertices = (GLfloat * len(vertices))(*vertices)

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)

    glUseProgram(shader_program)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    # Get uniform locations
    color_loc = glGetUniformLocation(shader_program, "color")
    rotation_loc = glGetUniformLocation(shader_program, "rotation")

    # Initialize color and rotation
    color = [1.0, 0.0, 0.0]  # Red
    rotation = 0.0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color = [1.0, 0.0, 0.0]  # Red
                elif event.key == pygame.K_g:
                    color = [0.0, 1.0, 0.0]  # Green
                elif event.key == pygame.K_b:
                    color = [0.0, 0.0, 1.0]  # Blue
                elif event.key == pygame.K_LEFT:
                    rotation -= 0.1
                elif event.key == pygame.K_RIGHT:
                    rotation += 0.1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Update uniforms
        glUniform3f(color_loc, *color)
        glUniform1f(rotation_loc, rotation)

        glDrawArrays(GL_TRIANGLES, 0, 3)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()