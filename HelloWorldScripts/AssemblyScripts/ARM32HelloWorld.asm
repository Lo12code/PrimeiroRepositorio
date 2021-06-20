.global _start
.section .text

_start:
	mov r7, #0x4
	mov r0, #2
	ldr r1, =message
	mov r2, #13
	swi 0

	mov r7, #0x01
	mov r0, #0
	swi 0

.section .data
	message:
	.ascii "Hello World!\n"