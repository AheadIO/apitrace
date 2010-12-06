##########################################################################
#
# Copyright 2008-2009 VMware, Inc.
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
##########################################################################/


"""WGL tracing code generator."""


from wglapi import wglapi
from trace import Tracer
from codegen import *


public_symbols = set([
	"glAccum",
	"glAlphaFunc",
	"glAreTexturesResident",
	"glArrayElement",
	"glBegin",
	"glBindTexture",
	"glBitmap",
	"glBlendFunc",
	"glCallList",
	"glCallLists",
	"glClear",
	"glClearAccum",
	"glClearColor",
	"glClearDepth",
	"glClearIndex",
	"glClearStencil",
	"glClipPlane",
	"glColor3b",
	"glColor3bv",
	"glColor3d",
	"glColor3dv",
	"glColor3f",
	"glColor3fv",
	"glColor3i",
	"glColor3iv",
	"glColor3s",
	"glColor3sv",
	"glColor3ub",
	"glColor3ubv",
	"glColor3ui",
	"glColor3uiv",
	"glColor3us",
	"glColor3usv",
	"glColor4b",
	"glColor4bv",
	"glColor4d",
	"glColor4dv",
	"glColor4f",
	"glColor4fv",
	"glColor4i",
	"glColor4iv",
	"glColor4s",
	"glColor4sv",
	"glColor4ub",
	"glColor4ubv",
	"glColor4ui",
	"glColor4uiv",
	"glColor4us",
	"glColor4usv",
	"glColorMask",
	"glColorMaterial",
	"glColorPointer",
	"glCopyPixels",
	"glCopyTexImage1D",
	"glCopyTexImage2D",
	"glCopyTexSubImage1D",
	"glCopyTexSubImage2D",
	"glCullFace",
#	"glDebugEntry",
	"glDeleteLists",
	"glDeleteTextures",
	"glDepthFunc",
	"glDepthMask",
	"glDepthRange",
	"glDisable",
	"glDisableClientState",
	"glDrawArrays",
	"glDrawBuffer",
	"glDrawElements",
	"glDrawPixels",
	"glEdgeFlag",
	"glEdgeFlagPointer",
	"glEdgeFlagv",
	"glEnable",
	"glEnableClientState",
	"glEnd",
	"glEndList",
	"glEvalCoord1d",
	"glEvalCoord1dv",
	"glEvalCoord1f",
	"glEvalCoord1fv",
	"glEvalCoord2d",
	"glEvalCoord2dv",
	"glEvalCoord2f",
	"glEvalCoord2fv",
	"glEvalMesh1",
	"glEvalMesh2",
	"glEvalPoint1",
	"glEvalPoint2",
	"glFeedbackBuffer",
	"glFinish",
	"glFlush",
	"glFogf",
	"glFogfv",
	"glFogi",
	"glFogiv",
	"glFrontFace",
	"glFrustum",
	"glGenLists",
	"glGenTextures",
	"glGetBooleanv",
	"glGetClipPlane",
	"glGetDoublev",
	"glGetError",
	"glGetFloatv",
	"glGetIntegerv",
	"glGetLightfv",
	"glGetLightiv",
	"glGetMapdv",
	"glGetMapfv",
	"glGetMapiv",
	"glGetMaterialfv",
	"glGetMaterialiv",
	"glGetPixelMapfv",
	"glGetPixelMapuiv",
	"glGetPixelMapusv",
	"glGetPointerv",
	"glGetPolygonStipple",
	"glGetString",
	"glGetTexEnvfv",
	"glGetTexEnviv",
	"glGetTexGendv",
	"glGetTexGenfv",
	"glGetTexGeniv",
	"glGetTexImage",
	"glGetTexLevelParameterfv",
	"glGetTexLevelParameteriv",
	"glGetTexParameterfv",
	"glGetTexParameteriv",
	"glHint",
	"glIndexMask",
	"glIndexPointer",
	"glIndexd",
	"glIndexdv",
	"glIndexf",
	"glIndexfv",
	"glIndexi",
	"glIndexiv",
	"glIndexs",
	"glIndexsv",
	"glIndexub",
	"glIndexubv",
	"glInitNames",
	"glInterleavedArrays",
	"glIsEnabled",
	"glIsList",
	"glIsTexture",
	"glLightModelf",
	"glLightModelfv",
	"glLightModeli",
	"glLightModeliv",
	"glLightf",
	"glLightfv",
	"glLighti",
	"glLightiv",
	"glLineStipple",
	"glLineWidth",
	"glListBase",
	"glLoadIdentity",
	"glLoadMatrixd",
	"glLoadMatrixf",
	"glLoadName",
	"glLogicOp",
	"glMap1d",
	"glMap1f",
	"glMap2d",
	"glMap2f",
	"glMapGrid1d",
	"glMapGrid1f",
	"glMapGrid2d",
	"glMapGrid2f",
	"glMaterialf",
	"glMaterialfv",
	"glMateriali",
	"glMaterialiv",
	"glMatrixMode",
	"glMultMatrixd",
	"glMultMatrixf",
	"glNewList",
	"glNormal3b",
	"glNormal3bv",
	"glNormal3d",
	"glNormal3dv",
	"glNormal3f",
	"glNormal3fv",
	"glNormal3i",
	"glNormal3iv",
	"glNormal3s",
	"glNormal3sv",
	"glNormalPointer",
	"glOrtho",
	"glPassThrough",
	"glPixelMapfv",
	"glPixelMapuiv",
	"glPixelMapusv",
	"glPixelStoref",
	"glPixelStorei",
	"glPixelTransferf",
	"glPixelTransferi",
	"glPixelZoom",
	"glPointSize",
	"glPolygonMode",
	"glPolygonOffset",
	"glPolygonStipple",
	"glPopAttrib",
	"glPopClientAttrib",
	"glPopMatrix",
	"glPopName",
	"glPrioritizeTextures",
	"glPushAttrib",
	"glPushClientAttrib",
	"glPushMatrix",
	"glPushName",
	"glRasterPos2d",
	"glRasterPos2dv",
	"glRasterPos2f",
	"glRasterPos2fv",
	"glRasterPos2i",
	"glRasterPos2iv",
	"glRasterPos2s",
	"glRasterPos2sv",
	"glRasterPos3d",
	"glRasterPos3dv",
	"glRasterPos3f",
	"glRasterPos3fv",
	"glRasterPos3i",
	"glRasterPos3iv",
	"glRasterPos3s",
	"glRasterPos3sv",
	"glRasterPos4d",
	"glRasterPos4dv",
	"glRasterPos4f",
	"glRasterPos4fv",
	"glRasterPos4i",
	"glRasterPos4iv",
	"glRasterPos4s",
	"glRasterPos4sv",
	"glReadBuffer",
	"glReadPixels",
	"glRectd",
	"glRectdv",
	"glRectf",
	"glRectfv",
	"glRecti",
	"glRectiv",
	"glRects",
	"glRectsv",
	"glRenderMode",
	"glRotated",
	"glRotatef",
	"glScaled",
	"glScalef",
	"glScissor",
	"glSelectBuffer",
	"glShadeModel",
	"glStencilFunc",
	"glStencilMask",
	"glStencilOp",
	"glTexCoord1d",
	"glTexCoord1dv",
	"glTexCoord1f",
	"glTexCoord1fv",
	"glTexCoord1i",
	"glTexCoord1iv",
	"glTexCoord1s",
	"glTexCoord1sv",
	"glTexCoord2d",
	"glTexCoord2dv",
	"glTexCoord2f",
	"glTexCoord2fv",
	"glTexCoord2i",
	"glTexCoord2iv",
	"glTexCoord2s",
	"glTexCoord2sv",
	"glTexCoord3d",
	"glTexCoord3dv",
	"glTexCoord3f",
	"glTexCoord3fv",
	"glTexCoord3i",
	"glTexCoord3iv",
	"glTexCoord3s",
	"glTexCoord3sv",
	"glTexCoord4d",
	"glTexCoord4dv",
	"glTexCoord4f",
	"glTexCoord4fv",
	"glTexCoord4i",
	"glTexCoord4iv",
	"glTexCoord4s",
	"glTexCoord4sv",
	"glTexCoordPointer",
	"glTexEnvf",
	"glTexEnvfv",
	"glTexEnvi",
	"glTexEnviv",
	"glTexGend",
	"glTexGendv",
	"glTexGenf",
	"glTexGenfv",
	"glTexGeni",
	"glTexGeniv",
	"glTexImage1D",
	"glTexImage2D",
	"glTexParameterf",
	"glTexParameterfv",
	"glTexParameteri",
	"glTexParameteriv",
	"glTexSubImage1D",
	"glTexSubImage2D",
	"glTranslated",
	"glTranslatef",
	"glVertex2d",
	"glVertex2dv",
	"glVertex2f",
	"glVertex2fv",
	"glVertex2i",
	"glVertex2iv",
	"glVertex2s",
	"glVertex2sv",
	"glVertex3d",
	"glVertex3dv",
	"glVertex3f",
	"glVertex3fv",
	"glVertex3i",
	"glVertex3iv",
	"glVertex3s",
	"glVertex3sv",
	"glVertex4d",
	"glVertex4dv",
	"glVertex4f",
	"glVertex4fv",
	"glVertex4i",
	"glVertex4iv",
	"glVertex4s",
	"glVertex4sv",
	"glVertexPointer",
	"glViewport",
	"wglChoosePixelFormat",
	"wglCopyContext",
	"wglCreateContext",
	"wglCreateLayerContext",
	"wglDeleteContext",
	"wglDescribeLayerPlane",
	"wglDescribePixelFormat",
	"wglGetCurrentContext",
	"wglGetCurrentDC",
	"wglGetDefaultProcAddress",
	"wglGetLayerPaletteEntries",
	"wglGetPixelFormat",
	"wglGetProcAddress",
	"wglMakeCurrent",
	"wglRealizeLayerPalette",
	"wglSetLayerPaletteEntries",
	"wglSetPixelFormat",
	"wglShareLists",
	"wglSwapBuffers",
	"wglSwapLayerBuffers",
	"wglSwapMultipleBuffers",
	"wglUseFontBitmapsA",
	"wglUseFontBitmapsW",
	"wglUseFontOutlinesA",
	"wglUseFontOutlinesW",
])

class WglTracer(Tracer):

    def get_function_address(self, function):
        #print 'DebugBreak();'
        if function.name in public_symbols:
            return '__GetProcAddress("%s")' % (function.name,)
        else:
            print '        if (!pwglGetProcAddress) {'
            print '            pwglGetProcAddress = (PwglGetProcAddress)__GetProcAddress("wglGetProcAddress");'
            print '            if (!pwglGetProcAddress)'
            print '                Trace::Abort();'
            print '        }'
            return 'pwglGetProcAddress("%s")' % (function.name,)

    extensions = [
        # GL_VERSION_1_2
        "GL_EXT_bgra",
        "GL_EXT_draw_range_elements",
        "GL_EXT_packed_pixels",
        "GL_EXT_rescale_normal",
        "GL_EXT_separate_specular_color",
        "GL_EXT_texture3D",
        "GL_SGIS_texture_edge_clamp",
        "GL_SGIS_texture_lod",

        # GL_VERSION_1_3
        "GL_ARB_multisample",
        "GL_ARB_multitexture",
        "GL_ARB_texture_border_clamp",
        "GL_ARB_texture_compression",
        "GL_ARB_texture_cube_map", # GL_EXT_texture_cube_map
        "GL_ARB_texture_env_add", #"GL_EXT_texture_env_add",
        "GL_ARB_texture_env_dot3",
        "GL_ARB_texture_env_combine",
        "GL_ARB_transpose_matrix",

        # GL_VERSION_1_4
        "GL_ARB_depth_texture",
        "GL_ARB_point_parameters", #"GL_EXT_point_parameters",
        "GL_ARB_shadow",
        "GL_ARB_texture_env_crossbar",
        "GL_ARB_texture_mirrored_repeat",
        "GL_ARB_window_pos",
        "GL_EXT_blend_color",
        "GL_EXT_blend_func_separate",
        "GL_EXT_blend_minmax",
        "GL_EXT_blend_subtract",
        "GL_EXT_fog_coord",
        "GL_EXT_multi_draw_arrays",
        "GL_EXT_secondary_color",
        "GL_EXT_stencil_wrap",
        "GL_EXT_texture_lod_bias",
        "GL_SGIS_generate_mipmap",
        "GL_NV_blend_square",

        # GL_VERSION_1_5
        "GL_ARB_occlusion_query",
        "GL_ARB_vertex_buffer_object",
        "GL_EXT_shadow_funcs",

        # GL_VERSION_2_0
        "GL_ARB_draw_buffers",
        "GL_ARB_fragment_program",
        "GL_ARB_fragment_shader",
        "GL_ARB_point_sprite",
        "GL_ARB_shader_objects",
        "GL_ARB_shading_language_100",
        "GL_ARB_texture_non_power_of_two",
        "GL_ARB_vertex_program",
        "GL_ARB_vertex_shader",
        "GL_EXT_blend_equation_separate",
        "GL_EXT_stencil_two_side",
    
        # GL_VERSION_2_1
        "GL_ARB_pixel_buffer_object", "GL_EXT_pixel_buffer_object",
        "GL_EXT_texture_sRGB",

        # XXX
        "GL_ARB_framebuffer_object", "GL_EXT_framebuffer_object",
        "GL_EXT_framebuffer_multisample",
        "GL_EXT_packed_depth_stencil",
        #"GL_EXT_texture_compression_s3tc",
        #"GL_S3_s3tc",
    ]

    wgl_extensions = [
        "WGL_ARB_extensions_string",
        "WGL_ARB_multisample",
        "WGL_ARB_pbuffer",
        "WGL_ARB_pixel_format",
        "WGL_EXT_extensions_string",
    ]

    def wrap_ret(self, function, instance):
        if function.name == "wglGetProcAddress":
            print '    if (%s) {' % instance
        
            func_dict = dict([(f.name, f) for f in wglapi.functions])

            def handle_case(function_name):
                f = func_dict[function_name]
                ptype = self.function_pointer_type(f)
                pvalue = self.function_pointer_value(f)
                print '    %s = (%s)%s;' % (pvalue, ptype, instance)
                print '    %s = (%s)&%s;' % (instance, function.type, f.name);
        
            def handle_default():
                print '    OS::DebugMessage("apitrace: unknown function \\"%s\\"\\n", lpszProc);'
                print '    %s = (%s)NULL;' % (instance, function.type);

            string_switch('lpszProc', func_dict.keys(), handle_case, handle_default)
            print '    }'

    def post_call_hook(self, function):
        if function.name == 'glGetString':
            print '    switch (name) {'
            print '    case GL_VENDOR:'
            print '        __result = (const GLubyte*)"VMware, Inc.";'
            print '        break;'
            print '    case GL_VERSION:'
            print '        __result = (const GLubyte*)"2.1";'
            print '        break;'
            print '    case GL_SHADING_LANGUAGE_VERSION:'
            print '        __result = (const GLubyte*)"1.2";'
            print '        break;'
            print '    case GL_EXTENSIONS:'
            print '        __result = (const GLubyte*)"%s";' % ' '.join(self.extensions)
            print '        break;'
            print '    default:'
            print '        break;'
            print '    }'

        if function.name == 'wglGetExtensionsStringARB':
            print '    return "%s";' % ' '.join(self.wgl_extensions)



if __name__ == '__main__':
    print
    print '#define _GDI32_'
    print
    print '#include "glimports.hpp"'
    print
    print '#include "trace_write.hpp"'
    print '#include "os.hpp"'
    print '#include "glsize.hpp"'
    print
    print 'extern "C" {'
    print '''
static HINSTANCE g_hDll = NULL;

static PROC
__GetProcAddress(LPCSTR lpProcName)
{
    if (!g_hDll) {
        char szDll[MAX_PATH] = {0};
        
        if (!GetSystemDirectoryA(szDll, MAX_PATH)) {
            return NULL;
        }
        
        strcat(szDll, "\\\\opengl32.dll");
        
        g_hDll = LoadLibraryA(szDll);
        if (!g_hDll) {
            return NULL;
        }
    }
        
    return GetProcAddress(g_hDll, lpProcName);
}

    '''
    tracer = WglTracer()
    tracer.trace_api(wglapi)
    print
    print '} /* extern "C" */'
