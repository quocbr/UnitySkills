# Unity Skills Workbench

Workbench sử dụng UnitySkills **3.0.0** của Besty.

Dự án Unity 6 cung cấp **một skill duy nhất, `$unity-skills`**, kết hợp hướng dẫn chính thức của Unity, các mẫu Unity 6.3 của Nice Wolf Studio và công cụ thao tác trực tiếp trong Editor của Besty. [Danh mục quy trình hợp nhất](unity-skills/references/workflows.md) bao gồm review C#, gameplay, Input System, ECS/DOTS, UI, CLI, vật lý, đồ họa và các nhóm tác vụ khác.

## Bắt đầu

1. Trong Unity Hub, chọn **Add project from disk** và mở thư mục này với Unity **6000.3.8f1**. Unity Package Manager sẽ nạp Besty từ mã nguồn trong dự án. Lần mở đầu có thể cần mạng để tải các package phụ thuộc từ registry của Unity.
2. Từ thư mục gốc, chạy lệnh sau với Python 3, rồi mở lại workspace trong Codex để nạp skills.

   ```powershell
   python scripts/install_skills.py --agent codex
   ```

   Dùng `--agent claude-code` cho Claude Code. Nếu đã cài bản tách rời, thêm `--migrate` để sao lưu các bản nhận diện được ra ngoài thư mục agent quét và thay bằng skill hợp nhất. Nếu muốn dùng Python client của Besty, cài `requests` trong môi trường Python của agent bằng `python -m pip install requests`.
3. Trong Unity, mở **Window > UnitySkills**, bật máy chủ và ghi lại cổng hiện trong bảng điều khiển. Ví dụ, nếu cổng là `8090`, kiểm tra bằng lệnh sau.

   ```powershell
   curl.exe http://localhost:8090/health
   ```

   Dùng đúng cổng của dự án nếu đang mở nhiều Editor. Khi yêu cầu agent ghi vào Editor, Besty kiểm tra instance đích và áp dụng chế độ quyền trong bảng UnitySkills.

UnitySkills dùng tiếng Việt mặc định khi chưa có tùy chọn ngôn ngữ đã lưu. Nếu đang dùng ngôn ngữ khác, mở **Settings > Pinned languages**, chọn **Vietnamese**, rồi bấm **VI** ở chân cửa sổ. Tên kỹ thuật Unity, tên tab như **AI Config**, và tên skill trong API giữ nguyên để dễ đối chiếu với Editor và tài liệu.

Thử yêu cầu trong Codex bằng `$unity-skills kiểm tra UI Toolkit của scene đang mở và đề xuất nơi gắn UIDocument cho HUD`. Skill sẽ dùng cùng một quy trình để xem cấu trúc UI, truy vấn Editor khi cần và kiểm tra cấu hình hiện có.

Trong Workbench, **Window > UnitySkills > AI Config** cũng đọc mẫu hợp nhất tại `unity-skills/`. Khi chuyển từ bản cũ, dùng script với `--migrate` để sao lưu trước khi cài.

## Dùng với một dự án Unity khác

Trong Unity của dự án đích, chọn **Package Manager → + → Install package from Git URL** và dán URL sau.

```text
https://github.com/quocbr/UnitySkills.git?path=/upstream/besty-unity-skills/SkillsForUnity#main
```

Mở **Window → UnitySkills → AI Config → Codex**, chọn **Cài đặt (Project)** hoặc **Cài đặt (Global)**. Gói đi kèm đúng mẫu `$unity-skills` hợp nhất và giao diện tiếng Việt. Bật **Khởi động Server** khi cần làm việc trực tiếp với Editor. Nếu đã cài skill hợp nhất ở chế độ Global, mở project trong Codex để sử dụng.

Cập nhật bằng cách dán lại cùng URL vào **Install package from Git URL**. Nếu đã tải repo về máy, có thể chọn **Install package from disk** và trỏ đến [package.json](upstream/besty-unity-skills/SkillsForUnity/package.json).

Sau khi cập nhật gói, dùng **AI Config → Cập nhật (Project)** hoặc **Cập nhật (Global)** cho agent đang dùng để nhận nội dung skill mới. Khi cài từ workspace bằng Python, thêm `--migrate` để sao lưu bản Workbench cũ trước khi thay thế.

Khi nâng cấp lên 3.0.0, UnitySkills chuyển lịch sử Workflow cũ sang `Library/UnitySkills/workflow_legacy/` và tự xóa bản lưu đó sau 14 ngày. [Ghi chú phát hành v3.0.0](https://github.com/Besty0728/Unity-Skills/releases/tag/v3.0.0)

### Tự gọi skill khi viết hoặc review C# trong Claude Code

Sau khi cài hoặc cập nhật skill cho **Claude Code** trong **AI Config**, mở **⚙ Cài đặt → Công cụ AI → Thêm hướng dẫn vào tệp chỉ dẫn của agent**. Với bản cài Project, Workbench thêm hướng dẫn vào `CLAUDE.md` ở gốc dự án. Mở lại Claude Code từ thư mục dự án để nạp hướng dẫn.

Thử gửi `Review JourneyPanel.cs, tìm nguyên nhân nút Use không chạy. Chỉ đọc.` mà không gõ `/unity-skills`. Hướng dẫn ưu tiên `unity-skills` cho tác vụ liên quan đến API, hành vi hoặc công cụ Unity. Khi chưa có hướng dẫn phù hợp, agent có thể dùng skill khác hoặc tiếp tục bằng quy trình coding và review thông thường. Xem lượt gọi skill trong phiên để kiểm tra.

## Bật hoặc tắt skill

Trong **Window → UnitySkills → Skills**, bỏ dấu chọn cạnh tên một skill hoặc cạnh tiêu đề nhóm để tắt. Chọn lại để bật. Lựa chọn được lưu riêng cho từng project. Khi bật lại một nhóm, trạng thái riêng của từng skill trong nhóm vẫn được áp dụng.

Các skill REST đã tắt bị ẩn khỏi danh mục API và bị chặn nếu agent gọi theo tên. Chế độ quyền của UnitySkills vẫn áp dụng cho các skill đang bật.

## Mã nguồn và giấy phép

| Thành phần | Bản nguồn đã ghim | Giấy phép |
| --- | --- | --- |
| [Skills chính thức](upstream/unity-technologies-skills/skills) | [`60f95e6`](https://github.com/Unity-Technologies/skills/tree/60f95e6d4beaeacf4dfdff7829ec9b35008a0be0) | [Unity Companion License](upstream/unity-technologies-skills/LICENSE.md) |
| [Gói Besty và Python client](upstream/besty-unity-skills/SkillsForUnity) | [`aa955d9`](https://github.com/Besty0728/Unity-Skills/tree/aa955d9ddf148b2fba1f46a4da2370004d9e2b36), v3.0.0 | [MIT](upstream/besty-unity-skills/LICENSE) |
| [Hướng dẫn Nice Wolf Studio](unity-skills/references/nice-wolf-studio) | [`a149d3e`](https://github.com/Nice-Wolf-Studio/unity-claude-skills/tree/a149d3e995420432f52b0899092daa4b069f441f) | [MIT](upstream/nice-wolf-studio-unity-claude-skills/LICENSE) |
| [Bộ kiểm tra `.meta`/GUID](upstream/gamedev-agent-skills/SOURCE.md) | [`2ee8518`](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/2ee85183666929223cc8b1bdb53da5e7d3fb4804), v2.0.0 | [Apache-2.0](upstream/gamedev-agent-skills/LICENSE), [NOTICE](upstream/gamedev-agent-skills/NOTICE) |

Mẫu `unity-skills/` giữ thông báo bản quyền và giấy phép của cả bốn nguồn. Tài liệu Nice Wolf Studio được mở theo chủ đề từ Workbench. Bộ kiểm tra `.meta`/GUID của awesome-gamedev-agent-skills là công cụ chỉ đọc cho lúc sửa asset ngoài Editor. Phần Unity Ops được tích hợp ở mức hướng dẫn chẩn đoán CLI, còn quyền thực thi tiếp tục do Workbench và agent kiểm soát. Unity Companion License áp dụng cho phần của Unity Technologies khi dùng với dự án phụ thuộc Unity. [Điều khoản Unity Companion License](https://unity.com/legal/licenses/unity-companion-license).
