#version 330 core

layout (location = 0) in vec3 aPos;

uniform float rotation;

void main()
{
    float s = sin(rotation);
    float c = cos(rotation);
    mat2 rotMat = mat2(c, -s, s, c);
    vec2 rotated = rotMat * aPos.xy;
    gl_Position = vec4(rotated, aPos.z, 1.0);
}