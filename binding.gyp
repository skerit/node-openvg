{
  'targets': [
    {
      'target_name': 'node-openvg',
      'sources': [
        'src/openvg.cc',
        'src/egl.cc'
      ],
      'ldflags': [
        "-L/opt/vc/lib",
        "-lGLESv2"
      ],
      'cflags': [
        "-DENABLE_GDB_JIT_INTERFACE",
        "-Wall",
        "-I/opt/vc/include",
        "-I/opt/vc/include/interface/vcos/pthreads"
      ],
    },
    {
      'target_name': 'init-egl',
      'sources': [
        'src/init-egl.cc'
      ],
      'ldflags': [
        "-L/opt/vc/lib",
        "-lGLESv2"
      ],
      'cflags': [
        "-DENABLE_GDB_JIT_INTERFACE",
        "-Wall",
        "-I/opt/vc/include",
        "-I/opt/vc/include/interface/vcos/pthreads"
      ],
    },
  ]
}
