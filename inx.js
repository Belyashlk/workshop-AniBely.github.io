const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

let likes = {
    avatar1 0,
    avatar2 0,
    avatar3 0,
    avatar4 0,
    avatar5 0,
    avatar6 0
};

 Получение количества лайков
app.get('likes', (req, res) = {
    res.json(likes);
});

 Обновление количества лайков
app.post('likes', (req, res) = {
    const { avatarId, count } = req.body;
    if (likes[avatarId] !== undefined) {
        likes[avatarId] = count;
        res.status(200).send('Likes updated');
    } else {
        res.status(400).send('Invalid avatar ID');
    }
});

app.listen(PORT, () = {
    console.log(`Server is running on httplocalhost${PORT}`);
});
