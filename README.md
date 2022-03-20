API Kode Pos Indonesia ini dibuat dengan sukarela, bisa digunakan jika bermanfaat. Lebih dari itu semoga bisa berkontribusi untuk mengembangkan API ini, terimakasih.

## Penggunaan di local server
```bash
git clone https://github.com/asepscareer/kodepos-api.git
```

```bash
cd kodepos-api && pip install -r requirements.txt
```

```bash
export FLASK_APP=main.py
flask run
```

# kodepos-api
kumpulan data kode pos negara Indonesia.

### penggunaan

<table>
<thead>
<tr>
  <th>No</th>
  <th>Keterangan</th>
  <th>Endpoint</th>
  <th>Parameter</th>
  <th>Method</th>
</tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>Get All Data Nasional</td>
    <td>/api/v1/get-data-nasional</td>
    <td>Tidak ada</td>
    <td>GET</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Get All Data Nasinal (Pagination)</td>
    <td>/api/v1/get-nasional?start={}&limit={}</td>
    <td>Ada</td>
    <td>GET</td>
  </tr>
  
  <tr>
    <td>3</td>
    <td>Get Daftar Provinsi</td>
    <td>/api/v1/daftar-daerah</td>
    <td>Tidak ada</td>
    <td>GET</td>
  </tr>
  
  <tr>
    <td>4</td>
    <td>Ekonomi</td>
    <td>/ekonomi</td>
    <td>Tidak ada</td>
    <td>GET</td>
  </tr>
  
  <tr>
    <td>5</td>
    <td>Get Data Provinsi</td>
    <td>/api/v1/get-data-provinsi/{}</td>
    <td>Ada</td>
    <td>GET</td>
  </tr>
  
  <tr>
    <td>6</td>
    <td>Setup Data Kode Pos Provinsi</td>
    <td>/api/v1/reset-data-provinsi</td>
    <td>Tidak ada</td>
    <td>GET</td>
  </tr>
  
  <tr>
    <td>7</td>
    <td>Setup Data Kode Pos Nasional</td>
    <td>/api/v1/reset-data-nasional</td>
    <td>Tidak ada</td>
    <td>GET</td>
  </tr>
 
</tbody>
</table>

### Postman Collection

[klik disini] (https://github.com/asepscareer/kodepost-api/blob/master/kodepos-api.json)

