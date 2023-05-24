<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Three.js Photo Frame with Raycaster</title>
  <style>
    body { margin: 0; }
    canvas { display: block; }
  </style>
</head>
<body>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/0.128.0/three.min.js"></script>
  <script>
    // Create a scene
    var scene = new THREE.Scene();

    // Create a camera
    var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 5;

    // Create a renderer
    var renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // Create a texture loader
    var textureLoader = new THREE.TextureLoader();

    // Load the photo frame texture
    var texture = textureLoader.load('photo_frame_texture.jpg');

    // Create the geometry for the photo frame
    var frameGeometry = new THREE.BoxGeometry(1.2, 1.2, 0.1);

    // Create the material for the photo frame
    var frameMaterial = new THREE.MeshBasicMaterial({ map: texture });

    // Create the photo frame mesh
    var frameMesh = new THREE.Mesh(frameGeometry, frameMaterial);
    scene.add(frameMesh);

    // Create a raycaster
    var raycaster = new THREE.Raycaster();
    var mouse = new THREE.Vector2();

    // Event listener for mouse clicks
    function onMouseClick(event) {
      // Calculate normalized device coordinates
      mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
      mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

      // Update the raycaster's position
      raycaster.setFromCamera(mouse, camera);

      // Check for intersections
      var intersects = raycaster.intersectObjects(scene.children);

      if (intersects.length > 0) {
        // The ray intersects an object
        console.log('Intersection:', intersects[0].object);
      }
    }

    // Attach the event listener to the document
    document.addEventListener('click', onMouseClick, false);

    // Animation loop
    function animate() {
      requestAnimationFrame(animate);

      // Rotate the photo frame
      frameMesh.rotation.y += 0.01;

      // Render the scene with the camera
      renderer.render(scene, camera);
    }

    // Start the animation loop
    animate();
  </script>
</body>
</html>
