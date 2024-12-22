
document.addEventListener("DOMContentLoaded", () => {
    const threadId = document.getElementById("thread-id").value;
   
    function fetchComments() {
        fetch(`/api/comments/${threadId}/`)
            .then(response => response.json())
            .then(data => {
                const container = document.getElementById("comments-container");
                container.innerHTML = "";
                data.forEach(comment => {
                    const commentElement = document.createElement("div");
                    commentElement.classList.add("comment");
                    commentElement.innerHTML = `
                        <p><strong>${comment.user}</strong> (${comment.created_at}): ${comment.content}</p>
                        <button class="comment-reply-btn" onclick="replyToComment(${comment.id})">Reply</button>
                    `;
                    container.appendChild(commentElement);

                    if (comment.replies.length > 0) {
                        const repliesContainer = document.createElement("div");
                        repliesContainer.classList.add("replies");
                        comment.replies.forEach(reply => {
                            const replyElement = document.createElement("div");
                            replyElement.innerHTML = `
                                <p><strong>${reply.user}</strong> (${reply.created_at}): ${reply.content}</p>
                            
                            `;
                            repliesContainer.appendChild(replyElement);
                        });
                        container.appendChild(repliesContainer);
                    }
                });
            });
    }

    document.getElementById("comment-form").addEventListener("submit", event => {
        event.preventDefault();
        const content = document.getElementById("comment-content").value;
        const parentId = document.getElementById("parent-id").value;

        fetch(`/api/comments/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ thread_id: threadId, content: content, parent_id: parentId }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById("comment-content").value = "";
                document.getElementById("parent-id").value = "";
                fetchComments();
            }
        });
    });

    fetchComments();
});

function replyToComment(commentId) {
    document.getElementById("parent-id").value = commentId;
    document.getElementById("comment-content").focus();
}
