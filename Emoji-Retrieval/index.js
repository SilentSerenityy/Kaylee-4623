const fetch = require("node-fetch")
const fs = require("fs")
const zipper = require('zip-local');
require("./server")

const emojiStart = /(<a:|<:)([a-zA-Z_0-9]*):/g
const emojiEnd = />/g
const isEmojiLink = /https:\/\/cdn.discordapp.com\/emojis\/([0-9]*)\?v=1/g
const getIdFromLink = (link) => link.replace("https://cdn.discordapp.com/emojis/", "").replace("?v=1", "")
//you can add as many as you want just seperate them with " "
newText = "<:PenguinGirlSnuggle:814623919680127017> <:PenguinGirlLayDown:814623919955902556> <:PenguinGirlSip:814623920027336745>".replace(emojiStart, "https://cdn.discordapp.com/emojis/").replace(emojiEnd, "?v=1")
emojiLinkList = newText.match(isEmojiLink)
for (const el of emojiLinkList) {
  fetch(el).then((img) => {
    img.buffer().then((buffer) => {
      fetch(el).then((img1) => {
        type = img1.headers.get('Content-Type')
        if (!type) {

        } else {
          itype = type.replace(/image\//g, "")
          if (buffer != "") {
            fs.writeFileSync(`./images/${getIdFromLink(el)}.${itype}`, buffer)
          }
        }
      })
    })
  })
}

zipper.sync.zip("./images").compress().save("images.zip");