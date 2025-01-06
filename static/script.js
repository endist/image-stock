document.addEventListener('DOMContentLoaded', () => {
  // console.log("DOM fully loaded and parsed"); // デバッグ: DOMがロードされたことを確認

  // Fetch the list of images from the server
  fetch('/images')
    .then(response => {
      // console.log("Fetching images"); // デバッグ: fetch呼び出しを確認
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json(); // レスポンスをJSONとして解析
    })
    .then(imageFiles => {
      // console.log('Received image list:', imageFiles); // デバッグ: 受信したJSONデータを出力

      const imageSelector = document.getElementById('image-selector');
      if (!imageSelector) {
        console.error("Error: #image-selector not found in the DOM"); // 要素が見つからない場合のエラー
        return;
      }

      // Populate the dropdown menu
      imageFiles.forEach(file => {
        const option = document.createElement('option');
        option.value = file;
        option.textContent = file;
        imageSelector.appendChild(option);
      });

      // Set initial background if there are images
      if (imageFiles.length > 0) {
        document.body.style.backgroundImage = `url('/images/${imageFiles[0]}')`;
      }

      // Change background image on selection
      imageSelector.addEventListener('change', (event) => {
        const selectedImage = event.target.value;
        document.body.style.backgroundImage = `url('/images/${selectedImage}')`;
      });
    })
    .catch(error => {
      console.error('Error fetching or processing image list:', error); // エラーログ
    });
});
