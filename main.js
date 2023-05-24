import * as THREE from 'three';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

const geometry = new THREE.BoxGeometry( 3, 6, 1 );
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
const cube = new THREE.Mesh( geometry, material );
scene.add( cube );

camera.position.z = 5;


const wallGroup = new THREE.Group();
scene.add(wallGroup);

const wall1 = new THREE.Mesh(geometry, material);
wall1.position.set(3, 6, 1);
wallGroup.add(wall1);

const wall2 = new THREE.Mesh(geometry, material);
wall2.position.set(8, 3, 1);
wallGroup.add(wall2);

const mesh1 = new THREE.Mesh(geometry, material);
mesh1.position.set(10, 0, 0);
scene.add(mesh1);

var wallMaterials = [
	new THREE.MeshBasicMaterial({ color: 0xff0000 }), // Red
	new THREE.MeshBasicMaterial({ color: 0x00ff00 }), // Green
	new THREE.MeshBasicMaterial({ color: 0x0000ff }), // Blue
	new THREE.MeshBasicMaterial({ color: 0xffff00 }), // Yellow
	new THREE.MeshBasicMaterial({ color: 0xff00ff })  // Magenta
  ];

  // Create the wall geometries
  var wallGeometry = new THREE.BoxGeometry(1, 1, 0.1);

  // Create the walls and assign materials
  var wall1 = new THREE.Mesh(wallGeometry, wallMaterials[0]);
  wall1.position.set(0, 0, -2);
  wallsGroup.add(wall1);

function animate() {
	requestAnimationFrame( animate );

	cube.rotation.x += 0.01;
	cube.rotation.y += 0.01;

	renderer.render( scene, camera );
}

animate();